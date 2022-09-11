from . import views
from django.urls import path

urlpatterns = [
    path('coffees/', views.CoffeeList.as_view(), name='coffee'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
    path('<slug:slug>/', views.CoffeeDetail.as_view(), name='coffee'),
    path('like/<slug:slug>', views.CoffeeLike.as_view(), name='coffee_like'),
]
