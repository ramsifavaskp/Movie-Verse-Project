from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        #check if the form is valid
        if form.is_valid():
            user = form.save()

            #get the raw password
            raw_password = form.cleaned_data.get('password1')

            #authenticate the user
            user = authenticate(username=user.username, password=raw_password)
            #login the user after registration
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect("main:home")

    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})

#login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #check the credentials
        user = authenticate(username=username, password=password)

        if user is not None:
             if user.is_active:
                login(request, user)
                messages.success(request, "You have successfully logined!")
                return redirect("main:home")
             else:
                return render(request, 'accounts/login.html', {'error': "Your Account has been disabled"})

        else:
            return render(request, 'accounts/login.html', {'error': "Invalid Username/Password"})

    return render(request, 'accounts/login.html')
#logout user
def logout_user(request):
    logout(request)
    return redirect("accounts:login")


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Assuming your user profile model is named UserProfile
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm  # Import your RegistrationForm
from .models import Profile  # Import your Profile model

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile  # Assuming a one-to-one relationship with Profile
    if profile.profile_img:
        profile_image_url = profile.profile_img.url
    else:
        profile_image_url = '/static/profile_pics/default.png'

    context = {
        'user': user,
        'profile': profile,
        'profile_image_url': profile_image_url,
    }

    return render(request, 'accounts/profile.html', context)

from django import forms
from .models import Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'bio','profile_img')  # Adjust fields as needed


@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile  # Assuming a one-to-one relationship with Profile

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)  # Update existing profile
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', username=user.username)  # Redirect to updated profile
    else:
        form = ProfileEditForm(instance=profile)  # Pre-populate form with existing data

    context = {
        'user': user,
        'profile': profile,
        'form': form,
    }
    return render(request, 'accounts/edit_profile.html', context)

