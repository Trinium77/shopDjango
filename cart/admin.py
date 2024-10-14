from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    fields = ('product', 'quantity', 'sub_total')  # Ajout du champ sub_total
    readonly_fields = ('sub_total',)  # Rendre le champ sub_total en lecture seule

    def sub_total(self, obj):
        """Calcule le sous-total pour cet article."""
        return obj.sub_total()
    sub_total.short_description = 'Sous-total'  # Titre du champ dans l'admin

class AdminCart(admin.ModelAdmin):
    list_display = ('user', 'total_items', 'total_price')  # Afficher le nombre total d'articles et le prix total
    inlines = [CartItemInline]

    def total_items(self, obj):
        """Retourne le nombre total d'articles dans le panier."""
        return obj.total_items()
    total_items.short_description = 'Total d\'articles'  # Titre du champ

    def total_price(self, obj):
        """Retourne le prix total des articles dans le panier."""
        return obj.total_price()
    total_price.short_description = 'Prix total'  # Titre du champ

admin.site.register(Cart, AdminCart)
