# shop/admin.py
from django.contrib import admin
from .models import Product, Comment

admin.site.site_header = "E-commerce"
admin.site.site_title = "SBC shop"
admin.site.index_title = "Gestion des produits"

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')  # Ajoutez 'category'
    search_fields = ('title',)
    list_editable = ('price',)

admin.site.register(Product, AdminProduct)
admin.site.register(Comment)
