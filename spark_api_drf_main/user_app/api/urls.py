from unicodedata import name
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user_app.api.views import regitration_view

urlpatterns = [
        path('login/', obtain_auth_token, name='login'),
        path('register/', regitration_view, name='register'),
]
