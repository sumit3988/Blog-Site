from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone

from .models import Post
from .forms import PostForm
from comments.forms import CommentForm


def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        status=Post.Status.PUBLISHED
    )

    comments = post.comments.filter(is_approved=True)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("posts:post-detail", slug=post.slug)
    else:
        form = CommentForm()

    return render(request, "posts/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })

@login_required
@permission_required("posts.add_post", raise_exception=True)
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("dashboard")
    else:
        form = PostForm()

    return render(request, "posts/post_form.html", {
        "form": form
    })

@login_required
@permission_required("posts.change_post", raise_exception=True)
def post_edit(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        author=request.user,
        status=Post.Status.DRAFT
    )

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:post-detail", slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, "posts/post_form.html", {
        "form": form,
        "is_edit": True
    })


@login_required
@permission_required("posts.delete_post", raise_exception=True)
def post_delete(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        author=request.user,
        status=Post.Status.DRAFT
    )

    if request.method == "POST":
        post.delete()
        return redirect("dashboard")

    return render(request, "posts/post_confirm_delete.html", {
        "post": post
    })


@login_required
@permission_required("posts.submit_post", raise_exception=True)
def submit_for_review(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        author=request.user,
        status=Post.Status.DRAFT
    )

    post.status = Post.Status.REVIEW
    post.save()

    return redirect("dashboard")


@login_required
@permission_required("posts.publish_post", raise_exception=True)
def publish_post(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        status=Post.Status.REVIEW
    )

    post.status = Post.Status.PUBLISHED
    post.reviewed_by=request.user
    post.save()

    return redirect("dashboard")
