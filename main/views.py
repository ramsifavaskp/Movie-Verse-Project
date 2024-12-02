from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from .forms import MovieForm
# Create your views here.



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.
#########
# Create your views here.
def home(request):
    query = request.GET.get("title")
    allMovies = None
    if query:
        allMovies = Movie.objects.filter(name__icontains=query)
    else:
        allMovies = Movie.objects.all()   # select * from movies
    #can use ,context dictionary instead {'movies': allMovies}
    return render(request, 'main/index.html', {'movies': allMovies}) #got error here, instead of using dictionary write in this way
from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Replace with your desired redirect URL
    else:
        form = CategoryForm()

    context = {'form': form}
    return render(request, 'main/create_category.html', context)

def movie_list(request):
    movies = Movie.objects.all().order_by('name')
    categories = Category.objects.all()
    
    return render(request, 'main/index.html', {'movies': movies, 'categories': categories})
from django.shortcuts import render, redirect
from .models import Movie, Category
from .forms import MovieForm


@login_required # Add if you require users to be logged in
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            # Access selected category object
            selected_category = form.cleaned_data['category']
            movie = form.save(commit=False)  # Prevent immediate save
            movie.category = selected_category  # Assign the category object
            movie.save()
            return redirect('/')
    # Replace with your desired redirect URL
    else:
        form = MovieForm()

    context = {'form': form}
    return render(request, 'main/addmovies.html', context)

def details(request, id):
    movie = Movie.objects.get(id=id)
    # Retrieve reviews for the specific movie
    reviews = Review.objects.filter(movie=id).order_by("-comment")
    average = reviews.aggregate()
    return render(request, 'main/details.html', {'movie': movie, 'reviews': reviews})


def add_review(request, id):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, id=id)
        user_review = Review.objects.filter(movie=movie, user=request.user).first()

        if user_review:
            # User has already submitted a review, show a message
            return render(request, 'main/details.html', {"movie": movie, "reviewed": True})

        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("main:details", id=id)
        else:
            form = ReviewForm()

        return render(request, 'main/details.html', {"movie": movie, "form": form})

    else:
        return redirect("accounts:login")
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def update_movie(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'Movie not found'})

    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        edit = form.save(commit=False)  # Save the form initially (including image)
        edit.category = form.cleaned_data['category']  # Assign category after initial save
        edit.save()  # Save again with the updated category
        return redirect('/', movie.id)

    return render(request, 'main/edit.html', {'form': form, 'movie': movie})

    # Display success message
    # or
    # return redirect('movie_list')  # Redirect to movie list

    return render(request, template_name, {'form': form})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'main/delete.html')

from django.shortcuts import render, redirect
from .models import Movie, Category
from .forms import MovieForm

def display_movies_by_category(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category', None)  # Get selected category from URL parameter

    if selected_category:
        movies = Movie.objects.filter(category_id=selected_category)  # Filter movies by category
    else:
        movies = Movie.objects.all()  # Show all movies if no category is selected
    context = {'categories': categories, 'movies': movies}
    return render(request, 'main/display_movies.html', context)

