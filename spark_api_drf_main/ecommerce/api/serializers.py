from rest_framework import serializers
from ecommerce.models import Category, Product, Customer, Order, OrderItem
from user_app.api.serializers import CustomUser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "category", "image"]

class CustomerSerializer(serializers.ModelSerializer):
    user = CustomUser()

    class Meta:
        model = Customer
        fields = ["id", "user", "address"]

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ["id", "product", "order", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "created_at", "updated_at", "order_items"]