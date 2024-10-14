from django.db import models
from django.conf import settings
from cart.models import Cart

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'En attente'),
        ('shipped', 'Expédié'),
        ('delivered', 'Livré'),
        ('cancelled', 'Annulé'),
    ], default='pending')

    def __str__(self):
        return f"Commande {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)  # Corrigé pour référencer le bon modèle
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
