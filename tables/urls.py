from django.urls import path
from tables import views


app_name = 'tables'

urlpatterns = [
    path('', views.TableListView.as_view(), name='list'),
    path('create/', views.TableCreateView.as_view(), name='create'),
    path('<int:pk>/', views.TableDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.TableEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.TableDeleteView.as_view(), name='delete'),
]
