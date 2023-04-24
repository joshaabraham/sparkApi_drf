from django.urls import path
from . import views

urlpatterns = [
    path("members/", views.MemberListCreateView.as_view(), name="member_list_create"),
    path("members/<int:pk>/", views.MemberRetrieveUpdateDestroyView.as_view(), name="member_detail"),

    path("sport_events/", views.SportEventListCreateView.as_view(), name="sport_event_list_create"),
    path("sport_events/<int:pk>/", views.SportEventRetrieveUpdateDestroyView.as_view(), name="sport_event_detail"),

    path("promotions/", views.PromotionListCreateView.as_view(), name="promotion_list_create"),
    path("promotions/<int:pk>/", views.PromotionRetrieveUpdateDestroyView.as_view(), name="promotion_detail"),

    path("subscriptions/", views.SubscriptionListCreateView.as_view(), name="subscription_list_create"),
    path("subscriptions/<int:pk>/", views.SubscriptionRetrieveUpdateDestroyView.as_view(), name="subscription_detail"),
]