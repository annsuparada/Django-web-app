from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #inherit UserRegisterForm
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #if form valid will be in dict
            messages.success(request, f'Your account has been created! You are now able to login') # reder success messages
            return redirect('login') #blog-home is the path name
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form": form})

@login_required #user must login to viwe this page
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    context = {
        'u_form': u_form,
        'p_form': p_form 
    }
    return render(request, 'users/profile.html', context)