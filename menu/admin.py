from django.contrib import admin
from menu.models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category']
    search_fields = ['title', 'category__name']
    list_filter = ['category']

