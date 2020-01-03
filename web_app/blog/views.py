from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    )
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

#LoginRequiredMixin will show login page and redirect to post/new 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
