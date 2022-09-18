from . import views
from django.urls import path


urlpatterns = [
    path('coffees/', views.coffees, name='coffees'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
    path('like/<slug:slug>', views.CoffeeLike.as_view(), name='coffee_like'),
    path('coffee_entries/', views.coffee_entries, name='coffee_entries'),
]
