from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorList.as_view(), name='actor_list'),
    path('actors/<int:pk>', views.ActorDetail.as_view(), name='actor_detail'),
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
    path('movie_cast/', views.MovieCastList.as_view(), name='movie_cast_list'),
    path('movie_cast/<int:pk>', views.MovieCastDetail.as_view(), name='movie_cast_detail'),
    path('genres/', views.GenreList.as_view(), name='genres_list'),
    path('genres/<int:pk>', views.GenreDetail.as_view(), name='genre_detail'),
    path('movie_genres/', views.MovieGenreList.as_view(), name='movie_genres_list'),
    path('movie_genres/<int:pk>', views.MovieGenreDetail.as_view(), name='movie_genre_detail'),
    path('reviewers/', views.ReviewerList.as_view(), name='reviewers_list'),
    path('reviewers/<int:pk>', views.ReviewerDetail.as_view(), name='reviewer_detail'),
    path('ratings/', views.RatingList.as_view(), name='ratings_list'),
    path('ratings/<int:pk>', views.RatingDetail.as_view(), name='rating_detail'),
    path('directors/', views.DirectorList.as_view(), name='directors_list'),
    path('directors/<int:pk>', views.DirectorDetail.as_view(), name='director_detail'),
    path('movie_directions/', views.MovieDirectionList.as_view(), name='movie_directions_list'),
    path('movie_directions/<int:pk>', views.MovieDirectionDetail.as_view(), name='movie_direction_detail'),
]