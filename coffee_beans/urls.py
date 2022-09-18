from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
    path('coffees/', views.coffees, name='coffees'),
    path('coffee_addition/', views.coffee_addition, name='coffee_addition'),
    path('like/<slug:slug>', views.CoffeeLike.as_view(), name='coffee_like'),
    path('<slug:slug>', views.CoffeeAdd.as_view(), name='coffee_add'),
]
