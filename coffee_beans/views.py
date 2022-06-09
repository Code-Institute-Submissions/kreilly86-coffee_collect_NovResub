from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1.)
    template_name = "coffees.html"


def home(request):
    return render(request, 'index.html')
  

def about(request):
    return render(request, 'about.html')
  

def join(request):
    return render(request, 'join.html')


def coffees(request):
    return render(request, 'coffees.html')


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1).order_by('-region')
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "coffees.html",
            {
                "post": post,
                "liked": liked,

            },
        )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('coffees', args=[slug]))
