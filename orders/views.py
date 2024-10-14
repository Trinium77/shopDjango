from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from cart.models import Cart
from django.http import JsonResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
import json

def create_order(request):
    if request.method == 'POST':
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return redirect('cart')  # Rediriger ou gérer le cas où il n'y a pas de panier

        with transaction.atomic():
            order = Order.objects.create(user=request.user, cart=cart)

            # Créer des OrderItems à partir des éléments du panier
            for item in cart.cartitem_set.all():
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

            # Optionnel : vider le panier après la commande
            cart.cartitem_set.all().delete()

        return redirect('order_summary', order_id=order.id)
    return render(request, 'orders/create_order.html')

def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_summary.html', {'order': order})

@csrf_exempt
def payments(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = get_object_or_404(Order, id=data['orderID'])

        # Mettez à jour le statut de la commande
        order.status = 'paid'  # Ou le statut approprié
        order.save()

        return JsonResponse({'order_number': order.id, 'transID': data['transID']})
