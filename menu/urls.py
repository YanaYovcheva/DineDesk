from django.urls import path, include
from menu import views

app_name = 'menu'

categories_paths = [
    path('', views.CategoryListView.as_view(), name='category-list'),
    path('add/', views.CategoryCreateView.as_view(), name='category-create'),
    path('<int:pk>/add-menuitem/', views.MenuItemCreateView.as_view(), name='menuitem-create'),
    path('detail/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('edit/<int:pk>', views.CategoryEditView.as_view(), name='category-edit'),
    path('delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category-delete'),
]

item_paths = [
    path('', views.MenuItemDetailView.as_view(), name='menuitem-detail'),
    path('edit/', views.MenuItemEditView.as_view(), name='menuitem-edit'),
    path('delete/', views.MenuItemDeleteView.as_view(), name='menuitem-delete'),
]

urlpatterns = [
    path('categories/', include(categories_paths)),
    path('item/<int:pk>/', include(item_paths)),
]
