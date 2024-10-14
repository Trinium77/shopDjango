from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),  # Vue par défaut
    # Utilise la vue `view_cart` pour afficher les détails du panier
    path('detail/', views.view_cart, name='cart_detail'),  
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
