from django.urls import path
from . import views


urlpatterns = [
    path('coffees/', views.coffees, name='coffees'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
    path('<slug:slug>/', views.CoffeeDetail.as_view(), name='coffees'),
    path('like/<slug:slug>', views.CoffeeLike.as_view(), name='coffees'),
]
