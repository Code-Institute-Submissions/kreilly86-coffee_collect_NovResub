from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Coffee
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
        'coffee_add': False,
    }
    return render(request, 'coffees.html', context)


class CoffeeList(generic.ListView):
    model = Coffee
    template_name = 'coffees.html'
    paginate_by = 6
    queryset = Coffee.objects.all()


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
        return HttpResponseRedirect(reverse('coffees', context))


class CoffeeAddition(View):

    def post(self, request, slug, *args, **kwargs):
        coffee = get_object_or_404(Coffee, slug=slug)
        coffee_entry = CoffeeEntry(data=request.POST) 
        if coffee_entry.is_valid():
            coffee = coffee_entry.save()
            coffee.save()
        else:
            coffee_entry = CoffeeEntry()

        return render(
            request,
            "coffee_addition.html",
            {
                "coffee": coffee,
                "coffee_entry": coffee_entry,
                "coffee_add": True,
            },
        )
