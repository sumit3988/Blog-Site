from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from posts.models import Post


def home(request):
    posts = Post.objects.filter(
        status=Post.Status.PUBLISHED
    ).order_by("-published_at")

    return render(request, "home.html", {"posts": posts})
