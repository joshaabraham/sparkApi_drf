from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryListCreateView.as_view(), name="category_list_create"),
    path("categories/<int:pk>/", views.CategoryRetrieveUpdateDestroyView.as_view(), name="category_detail"),
    path("products/", views.ProductListCreateView.as_view(), name="product_list_create"),
    path("products/<int:pk>/", views.ProductRetrieveUpdateDestroyView.as_view(), name="product_detail"),
    path("customers/", views.CustomerListCreateView.as_view(), name="customer_list_create"),
    path("customers/<int:pk>/", views.CustomerRetrieveUpdateDestroyView.as_view(), name="customer_detail"),
    path("orders/", views.OrderListCreateView.as_view(), name="order_list_create"),
    path("orders/<int:pk>/", views.OrderRetrieveUpdateDestroyView.as_view(), name="order_detail"),
    path("orderitems/", views.OrderItemListCreateView.as_view(), name="orderitem_list_create"),
    path("orderitems/<int:pk>/", views.OrderItemRetrieveUpdateDestroyView.as_view(), name="orderitem_detail"),
]