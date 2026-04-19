from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_account, name='create_account'),
    path('', views.get_accounts, name='get_accounts'),
    path('<int:account_id>/', views.get_account, name='get_account'),
]