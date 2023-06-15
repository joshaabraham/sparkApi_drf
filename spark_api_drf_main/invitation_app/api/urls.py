from django.urls import path
from .views import InvitationListCreateView, InvitationRetrieveUpdateDestroyView

urlpatterns = [
    path('invitations/', InvitationListCreateView.as_view(), name='invitations-list-create'),
    path('invitations/<int:pk>/', InvitationRetrieveUpdateDestroyView.as_view(), name='invitations-retrieve-update-destroy'),
]