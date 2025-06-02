from rest_framework import status
from rest_framework.generics import GenericAPIView
from .serializers import RegistrationSerializer
from rest_framework.response import Response

class RegistrationAPIView(GenericAPIView):
    serializer_class=RegistrationSerializer

    def post(self,requset,*args,**kwargs):
        serializer=RegistrationSerializer(data=requset.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data={'email':serializer.validated_data['email']}
        return Response(data,status=status.HTTP_201_CREATED)