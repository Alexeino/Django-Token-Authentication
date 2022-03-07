from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import  RegisterationSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework.authtoken.models import Token

class RegisterAPI(APIView):
    
    def post(self,request):
        print(request.user)
        serializer = RegisterationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            print(serializer.validated_data)
            user = serializer.save()
            data['response'] = "SUCCESS",
            data['username'] = user.username
            data['email'] = user.email
            token = Token.objects.create(user=user).key
            data['token'] = token
            print(data)
        else:
            data = serializer.errors
            data['response'] = "FAILED"
        return Response(data)