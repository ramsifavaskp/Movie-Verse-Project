"""
URL configuration for moviereview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
app_name="main"
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('details/<int:id>/', views.details, name="details"),
    path('add_movie/', views.add_movie, name="add_movie"),
    path('addreview/<int:id>', views.add_review, name='add_review'),
    path('update_movie/<int:id>/',views.update_movie,name='update_movie'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('create_category/',views.create_category,name='create_category'),
    path('display_movies_by_category/', views.display_movies_by_category, name='display_movies_by_category'),
]
if settings.DEBUG:
     urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
