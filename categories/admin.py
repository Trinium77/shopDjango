# categories/admin.py
from django.contrib import admin
from .models import Category

admin.site.site_header = "E-commerce"
admin.site.site_title = "SBC shop"
admin.site.index_title = "Gestion des catégories"

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')

admin.site.register(Category, AdminCategory)
