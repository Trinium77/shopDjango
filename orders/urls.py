# orders/urls.py
from django.urls import path
from .views import create_order, order_summary

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('summary/<int:order_id>/', order_summary, name='order_summary'),
]
