from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)

urlpatterns = [
    path(
        "", PostListView.as_view(), name="blog-home"
    ),  # Notice the method as_view() being called to turn class views into views
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path(
        "post/<int:pk>", PostDetailView.as_view(), name="post-detail"
    ),  # Notice that the route uses angle bracket syntax here to denote a variable being passed to the path - in this case the primary key, which should always be an integer
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("about/", views.about, name="blog-about"),
]
