from . import views
from django.urls import path

urlpatterns = [
    path('coffees/', views.PostList.as_view(), name='coffee'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
