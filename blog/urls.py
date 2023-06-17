from . import views
from django.urls import path


urlpatterns = [
    path('sports/', views.sports_view, name='sports'),
    path('music/', views.music_view, name='music'),
    path('art/', views.art_view, name='art'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<slug:post_slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='home')
]
