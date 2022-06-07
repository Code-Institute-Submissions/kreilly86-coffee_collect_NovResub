from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("coffees/", views.coffees, name="coffees"),
    path("about/", views.about, name="about"),
      path("join/", views.join, name="join"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='producer'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
