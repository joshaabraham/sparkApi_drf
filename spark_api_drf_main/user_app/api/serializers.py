from user_app.models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        CustomUser = get_user_model()
        model = CustomUser
        # fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'address', 'dob', 'mobile')
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True, 'required': False}}    
        
    def create(self, validated_data):
        CustomUser = get_user_model()
        user = CustomUser.objects.create_user(**validated_data)
        return user