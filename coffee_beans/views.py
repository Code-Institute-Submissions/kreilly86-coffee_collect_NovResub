from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Coffees


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def join(request):
    return render(request, 'join.html')


def coffees(request):
    return render(request, 'coffees.html')


class CoffeeDetail(View):

    def coffee(self, request, slug, *args, **kwargs):
        queryset = Coffees.objects.filter(status=1).order_by('-region')
        coffee = get_object_or_404(queryset, slug=slug)
        liked = False
        if coffee.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "coffees.html",
            {
                "coffee": coffee,
                "liked": liked,

            },
        )


class CoffeeLike(View):

    def coffee(self, request, slug):
        coffee = get_object_or_404(Coffee, slug=slug)
        if coffee.likes.filter(id=request.user.id).exists():
            coffee.likes.remove(request.user)
        else:
            coffee.likes.add(request.user)

        return HttpResponseRedirect(reverse('coffees', args=[slug]))
