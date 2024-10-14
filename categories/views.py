# categories/views.py
from django.shortcuts import render, get_object_or_404
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'categories/category_detail.html', {'category': category, 'products': products})
