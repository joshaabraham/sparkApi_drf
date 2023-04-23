from django.urls import path
from . import views

urlpatterns = [
    path("teams/", views.TeamListCreateView.as_view(), name="team_list_create"),
    path("teams/<int:pk>/", views.TeamRetrieveUpdateDestroyView.as_view(), name="team_detail"),
    path("players/", views.PlayerListCreateView.as_view(), name="player_list_create"),
    path("players/<int:pk>/", views.PlayerRetrieveUpdateDestroyView.as_view(), name="player_detail"),
]