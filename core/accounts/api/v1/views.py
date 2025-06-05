from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView
from .serializers import (RegistrationSerializer,CustomAuthTokenSerializer,CustomTokenObtainPairSerializer,ChangePasswordSerializer,
                          ProfileSerializer)
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ...models import Profile
from django.core.mail import send_mail

User=get_user_model()

class RegistrationAPIView(GenericAPIView):
    serializer_class=RegistrationSerializer
    ermission_classes=[IsAuthenticatedOrReadOnly]

    def post(self,requset,*args,**kwargs):
        serializer=RegistrationSerializer(data=requset.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data={'email':serializer.validated_data['email']}
        return Response(data,status=status.HTTP_201_CREATED)

class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class=CustomAuthTokenSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def post(self,request,*args,**kwargs):
        serializer=CustomAuthTokenSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token,created=Token.objects.get_or_create(user=user)
        return Response({'token':token.key,'user_id':user.pk,'email':user.email})

class CustomDiscardAuthToken(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        if not self.request.user.is_verified:
            return Response({'detail':'user is not verified'})
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer

class ChangePasswordAPIView(GenericAPIView):
    serializer_class= ChangePasswordSerializer
    permission_classes=[IsAuthenticated]
    model=User
    def get_object(self):
        obj=self.request.user
        return obj
    def put(self,request,*args,**kwargs):
        self.object=self.get_object()
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({'old_password':["wrong password"]},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response({'detail':'password successfully changed'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfileAPIView(RetrieveUpdateAPIView):
    serializer_class=ProfileSerializer
    queryset=Profile.objects.all()
    permission_classes=[IsAuthenticated]

    def get_object(self):
        queryset=self.get_queryset()
        obj=get_object_or_404(queryset,user=self.request.user)
        return obj

class TestEmailSend(GenericAPIView):
    def get(self,request,*args,**kwargs):
        send_mail('subject','message','from@example.com',['to@example.com'],fail_silently=False)
        return Response({'email sent'})