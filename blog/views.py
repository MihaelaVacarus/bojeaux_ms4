from django.shortcuts import render

from .models import Blog


def blog(request):
    """ A view to see the blog page """

    posts = Blog.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)
