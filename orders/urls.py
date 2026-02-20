from django.urls import path
from orders import views


app_name = 'orders'

urlpatterns = [
    path('create/<int:table_pk>/', views.OrderCreateView.as_view(), name='create'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='detail'),
    path('<int:order_pk>/add-item/', views.OrderItemCreateView.as_view(), name='add-item'),
    path('item/<int:pk>/delete/', views.OrderItemDeleteView.as_view(), name='delete-item'),
    path('<int:pk>/status/<str:status>/', views.OrderStatusEditView.as_view(), name='order-status'),
]
