from django.urls import path
from . import views

urlpatterns = [
    #route, file-name.function, 
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
