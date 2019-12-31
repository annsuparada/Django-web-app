from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMs',
        'title': 'Blog Post 1',
        'content': 'First post',
        'date_post': 'August, 10, 2018' 
    },
    {
        'author': 'Jane',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_post': 'August, 11, 2018' 
    },
] #dummy data 

def home(request):
    #pass dummy data to function by dict
    #then pass to third arg in render()
    context = {
        # 'key': data
        'posts': posts
    }
                        #sub dir of templates/HTML file
    return render(request, 'blog/home.html', context) 

def about(request):
    return render(request, 'blog/about.html')
