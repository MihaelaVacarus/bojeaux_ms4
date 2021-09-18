from django.contrib import admin
from django.db import models
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
    )


admin.site.register(Wishlist, WishlistAdmin)
