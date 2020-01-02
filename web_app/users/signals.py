from django.db.models.signals import post_save # post save signal when user is created
from django.contrib.auth.models import User #sender
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): #**kwargs is accept any argument 
    if created:
        Profile.objects.create(user=instance) #create profile when user is created

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


#explanation 26:28 - 
# https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8