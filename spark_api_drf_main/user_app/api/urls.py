from unicodedata import name
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path



# urlpatterns = [
#         path('login/', obtain_auth_token, name='login'),
# ]

from django.urls import path, include
from rest_framework import routers
from user_app.api import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = []
urlpatterns += router.urls
