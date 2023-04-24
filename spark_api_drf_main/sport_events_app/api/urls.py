from django.urls import path
from . import views

urlpatterns = [
    path("sport_events/", views.SportEventListCreateView.as_view(), name="sport_event_list_create"),
    path("sport_events/<int:pk>/", views.SportEventRetrieveUpdateDestroyView.as_view(), name="sport_event_detail"),
]