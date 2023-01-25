from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    BlogCreateView,
    BlogListView,
    BlogDeleteView,
)

app_name = 'blog'

urlpatterns = [
    # Para los Posts
    path('', PostListView.as_view(), name='home'),
    path('create/', PostCreateView.as_view(), name="create"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),

    # Para los Blogs
    path('list/', BlogListView.as_view(), name="blog_list"),
    path('create-blog/', BlogCreateView.as_view(), name="create_blog"),
    path("<int:pk>/delete-blog/", BlogDeleteView.as_view(), name="delete_blog")
]
