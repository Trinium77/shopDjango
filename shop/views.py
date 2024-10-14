from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Comment
from orders.models import Order, OrderItem  
from cart.models import Cart  
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from categories.models import Category  # Importer le modèle Category

def index(request):
    product_object = Product.objects.all()
    categories = Category.objects.all()  # Récupérer toutes les catégories
    item_name = request.GET.get('item-name')
    if item_name and item_name.strip():
        product_object = Product.objects.filter(title__icontains=item_name)

    paginator = Paginator(product_object, 8)  # Pour afficher 8 produits par page
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_object': product_object, 'categories': categories})

def detail(request, myid):
    product_object = get_object_or_404(Product, id=myid)
    comments = Comment.objects.filter(product=product_object).order_by('-created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(product=product_object, user=request.user, content=content)
            return redirect('detail', myid=myid)

    return render(request, 'shop/detail.html', {'product': product_object, 'comments': comments})

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)

    # Calcul des totaux
    total_price = sum(item.product.price * item.quantity for item in cart.cartitem_set.all())
    tax = total_price * 0.2  # Exemple de 20% de taxe
    grand_total = total_price + tax

    if request.method == "POST":
        user = request.user
        order = Order(user=user, cart=cart)
        order.save()

        # Créer les OrderItems à partir des éléments du panier
        for item in cart.cartitem_set.all():
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

        # Vider le panier après la commande
        cart.cartitem_set.all().delete()

        return redirect('confirmation')

    context = {
        'cart': cart,
        'total_price': total_price,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'shop/checkout.html', context)

def confirmation(request):
    info = Order.objects.order_by('-id')[:1]
    nom = info[0].user.username if info else 'Aucune commande trouvée'
    return render(request, 'shop/confirmation.html', {'name': nom})

def search(request):
    item_name = request.GET.get('item-name')
    products = Product.objects.filter(title__icontains=item_name) if item_name else Product.objects.all()
    return render(request, 'shop/search_results.html', {'products': products})

def about(request):
    return render(request, 'includes/about.html')  

def contact(request):
    return render(request, 'includes/contact.html')  

def products_by_category(request):
    categories = Category.objects.all()
    products_by_category = {category: category.products.all() for category in categories}
    return render(request, 'shop/products_by_category.html', {'products_by_category': products_by_category})
