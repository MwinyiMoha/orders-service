from django.contrib import admin

from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ["code", "customer", "status", "updated"]
    list_display_links = ["code"]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "item_total"]
    list_display_links = ["order"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
