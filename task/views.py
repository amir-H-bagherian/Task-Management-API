from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskReadSerializer, TaskCreateSerializer



class TaskViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(assigned_user=user)
    
    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TaskReadSerializer
        return TaskCreateSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(assigned_user=request.user)
        msg = "Task {} added successfully!".format(serializer.validated_data["title"])
        return Response({"message": msg}, status=status.HTTP_201_CREATED)
    
    @method_decorator(cache_page(60*60*2))
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        task = self.get_object()
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, pk):
        task = self.get_object()
        serializer = self.get_serializer(instance=task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        msg = "Task {} updated.".format(task.title)
        return Response({"message": msg}, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        task = self.get_object()
        task.delete()
        msg = "Task deleted successfully!"
        return Response(data={"message": msg}, status=status.HTTP_204_NO_CONTENT)