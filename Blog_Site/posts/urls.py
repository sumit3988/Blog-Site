from django.urls import path
from .views import post_detail

app_name="posts"

urlpatterns=[
    path("<slug:slug>/",post_detail, name="post-detail"),

]