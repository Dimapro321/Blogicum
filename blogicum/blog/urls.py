from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "posts/create/",
        views.create_post,
        name="create_post",
    ),
    path(
        "posts/<int:post_id>/",
        views.post_detail,
        name="post_detail",
    ),
    path(
        "posts/<int:post_id>/edit/",
        views.post_edit,
        name="edit_post",
    ),
    path(
        "posts/<int:post_id>/delete/",
        views.post_delete,
        name="delete_post",
    ),
    path(
        "posts/<int:post_id>/comment/",
        views.add_comment,
        name="add_comment",
    ),
    path(
        "posts/<int:post_id>/comments/" "<int:comment_id>/edit/",
        views.edit_comment,
        name="edit_comment",
    ),
    path(
        "posts/<int:post_id>/comments/" "<int:comment_id>/delete/",
        views.delete_comment,
        name="delete_comment",
    ),
    path(
        "profile/<str:username>/",
        views.profile,
        name="profile",
    ),
    path(
        "profile/<str:username>/edit/",
        views.edit_profile,
        name="edit_profile",
    ),
    path(
        "category/<slug:slug>/",
        views.category_posts,
        name="category_posts",
    ),
]
