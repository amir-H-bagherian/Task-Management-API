from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer


class RegisterView(APIView):
    
    def post(self, request):
        serializer = CustomUserSerializer(request.data)
        serializer.is_valid()
        serializer.save()
        return Response(data=serializer.validated_data, status=status.HTTP_201_CREATED)