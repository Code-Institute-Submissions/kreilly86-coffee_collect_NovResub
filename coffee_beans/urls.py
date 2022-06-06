from . import views
from django.urls import path

urlpatterns = [
    path("index.html", views.PostList.as_view(), name="home"),
    path("", views.PostList.as_view(), name="coffee"),
    path("about.html", views.PostList.as_view(), name="about"),
    path("join.html", views.PostList.as_view(), name="join"),
]
