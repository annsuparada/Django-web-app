from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    #pass dummy data to function by dict
    #then pass to third arg in render()
    context = {
        # 'key': value is the data
        'posts': Post.objects.all()
    }
                        #sub dir of templates/HTML file
    return render(request, 'blog/home.html', context) 

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_post']

class PostDetailView(DetailView):
    model = Post
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
