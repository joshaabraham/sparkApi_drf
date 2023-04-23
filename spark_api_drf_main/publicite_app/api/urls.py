from django.urls import path
from . import views

urlpatterns = [
    path("adcampaigns/", views.AdCampaignListCreateView.as_view(), name="adcampaign_list_create"),
    path("adcampaigns/<int:pk>/", views.AdCampaignRetrieveUpdateDestroyView.as_view(), name="adcampaign_detail"),
    path("ads/", views.AdListCreateView.as_view(), name="ad_list_create"),
    path("ads/<int:pk>/", views.AdRetrieveUpdateDestroyView.as_view(), name="ad_detail"),
]