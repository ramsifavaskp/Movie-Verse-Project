from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=254)  # Use built-in EmailField for validation
    profile_img = models.ImageField(upload_to='profile_pics/',default='default.png')
    bio = models.TextField(blank=True)# Optional profile picture

    def __str__(self):
        return f"{self.user.username}'s Profile"


