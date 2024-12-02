from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Make email required
    first_name = forms.CharField(max_length=150, required=True)  # Add first name field
    last_name = forms.CharField(max_length=150, required=True)  # Add last name field  # Optional profile picture

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=True)
        user.email = self.cleaned_data['email']  # Set email from form data
        if commit:
            user.save()
        profile = Profile.objects.create(user=user)  # Create profile after user creation
        profile.save()
        return user
