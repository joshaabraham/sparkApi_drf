from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from user_app.api.serializers import UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer