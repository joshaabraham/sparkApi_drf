from unicodedata import name
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path




from django.urls import path, include
from rest_framework import routers
from user_app.api import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
           path('auth/', obtain_auth_token, name='login'),
]
urlpatterns += router.urls
