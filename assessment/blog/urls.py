from django.urls import URLPattern, path
from .import views

urlpatterns = [
    path('blog/',views.index, name='blog-index'),
    path('post_detail/<int:pk>/',views.post_detail, name='blog-post-detail'),
    path('post_edit/<int:pk>/',views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>/',views.post_delete, name='blog-post-delete'),
    path('like/',views.like_post, name='blog-like_post'),
]