from django.urls import path
from .views import *
urlpatterns = [
    path("create_blog_post/", create_blog_post,name="blog_post_creation"),
    path("post/<int:pk>", blog_post_details,name="blog_post_details"),
    path("post/edit/<int:pk>", update_blog_post,name="update_post"),
    path("post/delete/<int:pk>", delete_blog_post,name="delete_post"),
    path("like/<int:pk>",like_post, name="like_post"),
    ]