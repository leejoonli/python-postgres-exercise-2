from django.shortcuts import render
from rest_framework import generics
from .serializers import ActorSerializer, MovieSerializer, MovieCastSerializer
from .models import Actor, Movie, MovieCast

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

# class List(generics.ListCreateAPIView):
# class Detail(generics.RetrieveUpdateDestroyAPIView):

# class List(generics.ListCreateAPIView):
# class Detail(generics.RetrieveUpdateDestroyAPIView):

# class List(generics.ListCreateAPIView):
# class Detail(generics.RetrieveUpdateDestroyAPIView):

# class List(generics.ListCreateAPIView):
# class Detail(generics.RetrieveUpdateDestroyAPIView):

# class List(generics.ListCreateAPIView):
# class Detail(generics.RetrieveUpdateDestroyAPIView):

# class List(generics.ListCreateAPIView):
# class Detail(generics.RetrieveUpdateDestroyAPIView):
