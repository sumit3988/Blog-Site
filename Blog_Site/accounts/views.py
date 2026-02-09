from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from posts.models import Post

@login_required
def dashboard(request):
    my_posts = Post.objects.filter(author=request.user)
    return render(request, "accounts/dashboard.html", {
        "posts": my_posts
    })
