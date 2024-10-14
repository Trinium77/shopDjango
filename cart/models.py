from django.db import models
from django.conf import settings
from shop.models import Product

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def total_items(self):
        """Retourne le nombre total d'articles dans le panier."""
        return sum(item.quantity for item in self.cartitem_set.all())

    def total_price(self):
        """Retourne le prix total des articles dans le panier."""
        return sum(item.sub_total() for item in self.cartitem_set.all())

    def __str__(self):
        return f"Panier de {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def sub_total(self):
        """Calcule le prix total pour cet article."""
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.title} ({self.quantity})"
