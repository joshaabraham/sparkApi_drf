from django.urls import path
from . import views

urlpatterns = [
    path("job_offers/", views.JobOfferListCreateView.as_view(), name="job_offer_list_create"),
    path("job_offers/<int:pk>/", views.JobOfferRetrieveUpdateDestroyView.as_view(), name="job_offer_detail"),

    path("job_searches/", views.JobSearchListCreateView.as_view(), name="job_search_list_create"),
    path("job_searches/<int:pk>/", views.JobSearchRetrieveUpdateDestroyView.as_view(), name="job_search_detail"),
]