"""Display the models in the admin panel"""

from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """ Products Data to display"""
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('-rating',)


class CategoryAdmin(admin.ModelAdmin):
    """ Categories Data to display"""
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """ Reviews Data to display"""
    fields = ('user',
              'text', 'rate', 'likes', 'unlikes',)

    list_display = (
        'user',
        'product',
        'date',
        'text',
        'rate',
        'likes',
        'unlikes',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
