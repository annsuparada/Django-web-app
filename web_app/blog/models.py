from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_post = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if the user got deleted, post got delete as well

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        #we're not using redirect() bc
        #reverse() will return full url to that route as a string