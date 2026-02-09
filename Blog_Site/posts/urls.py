from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("create/", views.post_create, name="post-create"),
    path("<slug:slug>/", views.post_detail, name="post-detail"),
    path("<slug:slug>/edit/",views.post_edit,name="post-edit"),
    path("<slug:slug>/delete/",views.post_delete,name="post-delete"),
    path("submit/<slug:slug>/",views.submit_for_review,name="post-submit")
]
