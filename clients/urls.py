from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_client, name='create_client'),
    path('', views.get_clients, name='get_clients'),
    path('<int:client_id>/', views.get_client, name='get_client'),
]