from django.urls import path

from menu import views

app_name = 'menu'

urlpatterns = [
    path('categories', views.CategoryListView.as_view(), name='category-list'),
    path('add/', views.CategoryCreateView.as_view(), name='category-create'),
    path('edit/<int:pk>', views.CategoryEditView.as_view(), name='category-edit' ),
    path('delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category-delete'),
]
