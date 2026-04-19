from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_transaction, name='create_transaction'),
    path('', views.get_transactions, name='get_transactions'),
    path('<int:transaction_id>/', views.get_transaction, name='get_transaction'),
]