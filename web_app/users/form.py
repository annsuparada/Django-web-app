from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#this form is inherit from Register class
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #keep configuration in one place
    class Meta:
        model = User
        #display field in what order
        fields = ['username', 'email', 'password1', 'password2']