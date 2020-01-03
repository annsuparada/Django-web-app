from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    #route, file-name.function, 
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'), #<pk> is primary key
    path('about/', views.about, name='blog-about'),
]
