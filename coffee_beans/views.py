from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Coffee
from .forms import CoffeeEntry


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contribute(request):
    return render(request, 'contribute.html')


def coffees(request):
    coffees_list = Coffee.objects.filter(approved=True)
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


def coffee_addition(request):
    coffee_entry = CoffeeEntry(data=request.POST)
    if coffee_entry.is_valid():
        coffee_entry.save()
        messages.success(request, "Thanks for submitting an entry. It is awaiting approval")
        return redirect(reverse('home'))
    else:
        coffee_entry = CoffeeEntry()

    template = 'coffee_addition.html'
    context = {
        'coffee_entry': coffee_entry
    }

    return render(request, template, context)
