from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import RegistrationSerializer,CustomAuthTokenSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

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
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)