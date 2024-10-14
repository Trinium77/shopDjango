from django.urls import path
from .views import index, detail, checkout, confirmation, search, about, contact, products_by_category

urlpatterns = [
    path('', index, name='home'),
    path('produits/', products_by_category, name='products_by_category'),  # Nouvelle URL
    path('detail/<int:myid>/', detail, name='detail'),
    path('checkout/', checkout, name='checkout'),
    path('confirmation/', confirmation, name='confirmation'),
    path('search/', search, name='search'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
