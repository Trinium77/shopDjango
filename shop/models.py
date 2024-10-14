# shop/models.py
from django.db import models
from django.conf import settings
from categories.models import Category  # Importez le modèle Category

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')  # Spécifiez un chemin
    date_added = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name='products')  # Ajoutez null=True

    def __str__(self):
        return self.title

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire par {self.user.username} sur {self.product.title}"
