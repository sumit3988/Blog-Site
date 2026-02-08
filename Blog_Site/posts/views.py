from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Post

def post_detail(request, slug):
    post=get_object_or_404(
        Post,
        slug=slug,
        status=Post.Status.PUBLISHED
    )

    return render (request, "posts/post_detail.html",{"post": post})