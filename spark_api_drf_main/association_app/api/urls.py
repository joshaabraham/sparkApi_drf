from django.urls import path
from . import views

urlpatterns = [
    path("membersCreate/", views.MemberListCreateView.as_view(), name="member_create"),
    path("member/<int:pk>/", views.MemberRetrieveUpdateDestroyView.as_view(), name="member_detail"),

    path("sport_eventsCreate/", views.SportEventListCreateView.as_view(), name="sport_event_create"),
    path("sport_event/<int:pk>/", views.SportEventRetrieveUpdateDestroyView.as_view(), name="sport_event_detail"),

    path("promotionCreate/", views.PromotionListCreateView.as_view(), name="promotion_create"),
    path("promotion/<int:pk>/", views.PromotionRetrieveUpdateDestroyView.as_view(), name="promotion_detail"),

    path("subscriptionsAssocCreate/", views.SubscriptionListCreateView.as_view(), name="subscription_create"),
    path("subscriptionAssoc/<int:pk>/", views.SubscriptionRetrieveUpdateDestroyView.as_view(), name="subscription_detail"),
]