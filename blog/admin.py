from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'image',
        'content',
        'created_on',
    )


admin.site.register(Blog, BlogAdmin)
