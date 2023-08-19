from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 
                  'first_name',
                  'last_name',
                  'password')
        
    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        user.set_password(validated_data.get('password'),)
        user.save()
        return user
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('password')
        rep.pop('id')
        rep['message'] = "User Created Successfully!"
        return rep
    
class CustomUserReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id', 'email')