from django.contrib import admin
from orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['table', 'status', 'created_at']
    list_filter = ['status', 'created_at']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menu_item', 'quantity']
    list_filter = ['menu_item']
    search_fields = ['menu_item__title']
