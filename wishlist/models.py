from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    user_profile = models.ForeignKey(
        'profiles.UserProfile', on_delete=models.CASCADE,
        null=False, blank=False, related_name='wishlist')

    products = models.ManyToManyField('products.Product')

    def __str__(self):
        return f"{self.user_profile}'s Wishlist"
