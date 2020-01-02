from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model): #inherat from user models
    user = models.OneToOneField(User, on_delete=models.CASCADE) #if user get deleted, profile got deleted too
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #upload to img directory

    def __str__(self):
        return f'{self.user.username} Profile'


