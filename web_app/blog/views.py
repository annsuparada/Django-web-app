from django.shortcuts import render
from django.http import HttpResponse
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

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
