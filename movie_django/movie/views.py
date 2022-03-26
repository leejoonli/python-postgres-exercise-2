from django.shortcuts import render
from rest_framework import generics
from .serializers import ActorSerializer, MovieSerializer, MovieCastSerializer, GenreSerializer, MovieGenreSerializer, ReviewerSerializer, RatingSerializer, DirectorSerializer, MovieDirectionSerializer
from .models import Actor, Movie, MovieCast, Genre, MovieGenre, Reviewer, Rating, Director, MovieDirection

# Create your views here.
class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCastList(generics.ListCreateAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializer

class MovieCastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieGenreList(generics.ListCreateAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class = MovieGenreSerializer

class MovieGenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class = MovieGenreSerializer

class ReviewerList(generics.ListCreateAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class ReviewerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieDirectionList(generics.ListCreateAPIView):
    queryset = MovieDirection.objects.all()
    serializer_class = MovieDirectionSerializer
    
class MovieDirectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieDirection.objects.all()
    serializer_class = MovieDirectionSerializer
