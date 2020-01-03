from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
    )
from . import views

urlpatterns = [
    #route, file-name.function, 
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'), #<pk> is primary key
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]


#create form is expect name of the model follow by _form.html
#so we create post_form.html for post-create