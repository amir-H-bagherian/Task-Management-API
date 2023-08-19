from rest_framework import serializers

from .models import Task
from account.serializers import CustomUserReadSerializer


class TaskCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ('title', 'description',
                  'status', 'assigned_user')
        
class TaskReadSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user_full_name')
    
    class Meta:
        model = Task
        fields = ('title', 'status', 'user')
        
    def get_user_full_name(self, obj):
        return obj.assigned_user.get_full_name()