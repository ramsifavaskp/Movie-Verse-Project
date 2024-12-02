from django import forms
from .models import *

#movie add form

from django import forms
from .models import Movie
from .models import Category
from django import forms
from .models import Category
from django import forms
from .models import Category, Movie

from django import forms
from .models import Movie, Category
from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
class MovieForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Movie
        fields = ['name', 'director', 'cast', 'release_date', 'description', 'rating', 'image', 'youtube_url', 'category']
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")
