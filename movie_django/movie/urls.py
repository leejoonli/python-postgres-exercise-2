from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorList.as_view(), name='actor_list'),
    path('actors/<int:pk>', views.ActorDetail.as_view(), name='actor_detail'),
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
    path('movie_cast/', views.MovieCastList.as_view(), name='movie_cast_list'),
    path('movie_cast/<int:pk>', views.MovieCastDetail.as_view(), name='movie_cast_detail'),
]