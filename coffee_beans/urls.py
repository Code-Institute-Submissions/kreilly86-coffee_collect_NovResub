from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contribute/', views.contribute, name='contribute'),
    path('coffees/', views.coffees, name='coffees'),
    path('coffee_addition/', views.coffee_addition, name='coffee_addition'),
    path('like/<slug:slug>', views.CoffeeLike.as_view(), name='coffee_like'),
    path('edit/<slug:slug>', views.edit_coffee, name='edit'),
    path('delete/<slug:slug>', views.delete_coffee, name='delete'),
]
