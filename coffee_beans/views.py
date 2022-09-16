from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Coffee


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def join(request):
    return render(request, 'join.html')


def coffees(request):
    coffees_list = Coffee.objects.all() 
  
    context = {
        'coffees': coffees_list,
    }
    return render(request, 'coffees.html', context)


class CoffeeLike(View):

    def post(self, request, slug, *args, **kwargs):
        coffee = get_object_or_404(Coffee, slug=slug)
        liked = False
        if coffee.likes.filter(id=request.user.id).exists():
            liked = True
            coffee.likes.remove(request.user)
        else:
            coffee.likes.add(request.user)

        context = {
            "coffee": coffee,
            "liked": liked,
        }
        return HttpResponseRedirect(reverse('coffees'))
