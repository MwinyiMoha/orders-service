from rest_framework import serializers

from .models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = OrderItem
        exclude = ["created", "updated"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    order_info = serializers.DictField(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
