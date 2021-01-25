"""Define the structure of stored data"""

from django.db import models
from django.contrib.auth.models import User


# Category Model
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
                                     null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Product Model
class Product(models.Model):
    category = models.ForeignKey('Category',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


RATE_CHOICES = [
    (1, '1 - Trash'),
    (2, '2 - Edible'),
    (3, '3 - I had Better'),
    (4, '4 - Fantastic'),
    (5, '5 - Amazing'),
]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    likes = models.PositiveIntegerField(default=0)
    unlikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
