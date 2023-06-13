from django.urls import path
from .views import UserActionListCreateView, UserActionRetrieveUpdateDestroyView

urlpatterns = [
    path('useractions/', UserActionListCreateView.as_view(), name='useractions-list-create'),
    path('useractions/<int:pk>/', UserActionRetrieveUpdateDestroyView.as_view(), name='useractions-retrieve-update-destroy'),
]