"""Afisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from movie_app.views import *
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/directors/', director_view),
    path('api/v1/directors/', DirectorListCreateAPIView.as_view()),
    # path('api/v1/directors/<int:id>/', director_details_views),
    path('api/v1/directors/<int:pk>/', DirectorRetrieveUpdateDestroyAPIView.as_view()),
    # path('api/v1/movies/', movie),
    path('api/v1/movies/', MovieListCreateAPIView.as_view()),
    path('api/v1/movies/<int:id>/', movie_details_views),
    # path('api/v1/reviews/', review),`
    path('api/v1/reviews/', ReviewListCreateAPIView.as_view()),
    # path('api/v1/reviews/<int:id>/', review_details_views),
    path('api/v1/reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view()),
    # path('api/v1/movies/reviews/', movies_review_views),
    path('api/v1/movies/reviews/', MoviesReviewListAPIView.as_view()),
    path('api/v1/user/', include('user.url'))
]
urlpatterns += swagger.urlpatterns
