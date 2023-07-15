from django.urls import path
from blog import views
from .views import DeletePost
from .views import TrendingPosts, PostDetail

urlpatterns = [
    path('sports/', views.sports_view, name='sports'),
    path('music/', views.music_view, name='music'),
    path('art/', views.art_view, name='art'),
    path('gaming/', views.gaming_view, name='gaming'),
    path('create_posts/', views.create_posts, name='create_posts'),
    path('post/<slug:slug>/delete/', DeletePost.as_view(), name='delete_post'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('trending/', TrendingPosts.as_view(), name='trending_posts'),
    path('<slug:post_slug>/', PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='home'),
]