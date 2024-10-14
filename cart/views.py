from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Vérifier si l'article est déjà dans le panier
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if created:
        cart_item.quantity = 1
    else:
        cart_item.quantity += 1
    cart_item.save()  # Met à jour la quantité

    messages.success(request, f"Le produit {product.title} a été ajouté au panier.")

    return redirect('home')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'cart': cart,
        'total_price': cart.total_price(),
        'total_items': cart.total_items(),
    }
    return render(request, 'cart/cart_detail.html', context)

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    messages.success(request, f"Le produit {cart_item.product.title} a été retiré du panier.")
    return redirect('cart:view_cart')
