from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required
from .models import Comment

@permission_required("comments.change_comment", raise_exception=True)
def pending_comments(request):
    comments = Comment.objects.filter(is_approved=False).select_related("post", "user")
    return render(request, "comments/pending_comments.html", {
        "comments": comments
    })

@permission_required("comments.change_comment", raise_exception=True)
def approve_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.is_approved = True
    comment.save()
    return redirect("comments:pending")

@permission_required("comments.delete_comment", raise_exception=True)
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect("comments:pending")
