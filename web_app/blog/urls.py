from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    #route, file-name.function, 
    path('', PostListView, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
