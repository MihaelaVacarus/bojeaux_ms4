from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
       'sku',
       'name',
       'category',
       'description',
       'ingredients',
       'price',
       'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
       'friendly_name',
       'name',
       'pk',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
