from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserReadSerializer

    
class CustomUserListCreateView(generics.ListCreateAPIView):
    permission_classes = []
    
    def get_queryset(self):
        return CustomUser.objects.filter(is_deleted=False)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomUserSerializer
        return CustomUserReadSerializer