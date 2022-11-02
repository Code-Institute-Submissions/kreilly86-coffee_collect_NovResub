from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Coffee
from .forms import CoffeeEntry


def home(request):
    """A view to return the index page"""
    return render(request, 'index.html')


def about(request):
    """A view to return the about page"""
    return render(request, 'about.html')


def contribute(request):
    """A view to return the contribute page"""
    return render(request, 'contribute.html')


def coffees(request):
    """A view to display Coffee Entries"""
    coffees_list = Coffee.objects.filter(approved=True)
    context = {
        'coffees': coffees_list,
    }
    return render(request, 'coffees.html', context)


class CoffeeLike(View):
    """A view to enable users to Like/Unlike coffee
    entries"""
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
    """A view to add Coffees to the Database"""
    coffee_entry = CoffeeEntry(data=request.POST)
    if coffee_entry.is_valid():
        coffee_entry = coffee_entry.save(commit=False)
        coffee_entry.user = request.user
        coffee_entry.save()
        messages.success(request, "Thanks for submitting an entry. It is awaiting approval")
        return redirect(reverse('coffees'))
    else:
        coffee_entry = CoffeeEntry()

    template = 'coffee_addition.html'
    context = {
        'coffee_entry': coffee_entry
    }

    return render(request, template, context)


@login_required
def edit_coffee(request, slug):
    """A view to Edit Coffee Entries"""
    coffee = get_object_or_404(Coffee, slug=slug)
    if request.method == 'POST':
        coffee_entry = CoffeeEntry(request.POST, instance=coffee)
        if coffee_entry.is_valid():
            coffee_entry = coffee_entry.save(commit=False)
            coffee_entry.user = request.user
            coffee_entry.save()
            messages.success(request, "Your entry has been updated")
            return redirect('coffees')
        else:
            messages.warning(request, "You are not authorised to edit this entry")

    coffee_entry = CoffeeEntry(instance=coffee)
    context = {
        "coffee_entry": coffee_entry
    }
    return render(request, 'edit_coffee.html', context)


def delete_coffee(request, slug):
    """A view to Delete Coffee Entry From Database"""
    if request.user.is_authenticated:
        coffee = get_object_or_404(Coffee, slug=slug)
        coffee.delete()
        messages.success(request, "Your entry has been deleted")
    else:
        messages.warning(request, "You are not authorised to delete entries")

    return redirect('coffees')
