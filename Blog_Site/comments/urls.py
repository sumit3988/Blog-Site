from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("pending/", views.pending_comments, name="pending"),
    path("approve/<int:comment_id>/", views.approve_comment, name="approve"),
    path("delete/<int:comment_id>/", views.delete_comment, name="delete"),
]
