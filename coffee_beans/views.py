from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Coffee, slugify
from .forms import CoffeeEntry


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
        if coffee.likes.filter(id=request.user.id).exists():
            coffee.likes.remove(request.user)
        else:
            coffee.likes.add(request.user)

        return HttpResponseRedirect(reverse('coffees'))

def coffee_addition(request):
    
    coffee_entry = CoffeeEntry(data=request.POST)
    if coffee_entry.is_valid():
        coffee_entry.save() 
    else:
        coffee_entry = CoffeeEntry()

    return render(
        request,
        "coffee_addition.html",
        {
            "coffee_entry": coffee_entry,
        },
    )
