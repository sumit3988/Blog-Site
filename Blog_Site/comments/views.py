from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied

from .models import Comment
from posts.models import Post


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    Comment.objects.create(
        post=post,
        user=request.user,
        content=request.POST.get("content")
    )

    return redirect("post-detail", pk=post.id)


@permission_required("comments.moderate_comment", raise_exception=True)
def approve_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.is_approved = True
    comment.save()
    return redirect("comment-queue")
