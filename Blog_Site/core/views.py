from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post

def home(request):
    posts = Post.objects.filter(
        status=Post.Status.PUBLISHED
    ).order_by("-published_at")

    return render(request, "home.html", {"posts": posts})


@login_required
def dashboard(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "accounts/dashboard.html", {
        "posts": posts
    })
