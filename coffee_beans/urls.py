from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='producer'),
    path('coffees.html', views.PostList.as_view(), name='coffee'),
    path('about.html', views.PostList.as_view(), name='about'),
    path('join.html', views.PostList.as_view(), name='join'),
]
