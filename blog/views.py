from django.shortcuts import render, get_object_or_404

from .models import Blog


def blog(request):
    """ A view to see the blog page """

    posts = Blog.objects.all().order_by('-created_on')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_post(request, slug):
    """ A view to see each blog post """

    blog = get_object_or_404(Blog, slug=slug)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_post.html', context)
