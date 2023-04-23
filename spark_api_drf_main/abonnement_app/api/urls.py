from django.urls import path
from . import views

urlpatterns = [
    path("subscriptions/", views.SubscriptionListCreateView.as_view(), name="subscription_list_create"),
    path("subscriptions/<int:pk>/", views.SubscriptionRetrieveUpdateDestroyView.as_view(), name="subscription_detail"),
    path("payments/", views.PaymentListCreateView.as_view(), name="payment_list_create"),
    path("payments/<int:pk>/", views.PaymentRetrieveUpdateDestroyView.as_view(), name="payment_detail"),
]