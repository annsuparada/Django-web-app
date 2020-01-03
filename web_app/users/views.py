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
    if request.method == 'POST': #if form are valid, we save that info
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #poputate current user info
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() 
            messages.success(request, f'Your account has been updated') # reder success messages
            return redirect('profile') 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form 
    }
    return render(request, 'users/profile.html', context)