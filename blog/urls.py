from django.urls import path
from blog import views

urlpatterns = [
    path('sports/', views.sports_view, name='sports'),
    path('music/', views.music_view, name='music'),
    path('art/', views.art_view, name='art'),
    path('gaming/', views.gaming_view, name='gaming'),
    path('create_posts/', views.create_posts, name='create_posts'),
    path('delete_post/<slug:slug>/', views.DeletePost.as_view(), name='delete_post'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('post/<slug:post_slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='home'),
]