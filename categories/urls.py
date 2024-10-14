# categories/urls.py
from django.urls import path
from .views import category_list, category_detail

urlpatterns = [
    path('', category_list, name='category_list'),
    path('<int:category_id>/', category_detail, name='category_detail'),
]
