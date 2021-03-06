from rest_framework import serializers
from .models import Actor, Movie, MovieCast, Genre, MovieGenre, Reviewer, Rating, Director, MovieDirection

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    actor = serializers.HyperlinkedRelatedField(view_name='actor_detail', read_only=True)
    actor_url = serializers.ModelSerializer.serializer_url_field(view_name='actor_detail')

    class Meta:
        model = Actor
        fields = ('id', 'fname', 'lname', 'gender', 'actor', 'actor_url')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedRelatedField(view_name='movie_detail', read_only=True)
    movie_url = serializers.ModelSerializer.serializer_url_field(view_name='movie_detail')
    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'time', 'language', 'release_date', 'release_country', 'movie', 'movie_url')

class MovieCastSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedRelatedField(view_name='movie_detail', read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        source='movie'
    )
    actor = serializers.HyperlinkedRelatedField(view_name='actor_detail', read_only=True)
    actor_id = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        source='actor'
    )
    class Meta:
        model = MovieCast
        fields = ('id', 'role', 'movie', 'movie_id', 'actor', 'actor_id')

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.HyperlinkedRelatedField(view_name='genre_detail', read_only=True)
    genre_url = serializers.ModelSerializer.serializer_url_field(view_name='genre_detail')

    class Meta:
        model = Genre
        fields = ('id', 'genre', 'genre_url', 'title')

class MovieGenreSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedRelatedField(view_name='movie_detail', read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        source='movie'
    )
    genre = serializers.HyperlinkedRelatedField(view_name='genre_detail', read_only=True)
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        source='genre'
    )
    class Meta:
        model = MovieGenre
        fields = ('id', 'movie', 'movie_id', 'genre', 'genre_id')

class ReviewerSerializer(serializers.HyperlinkedModelSerializer):
    reviewer = serializers.HyperlinkedRelatedField(view_name='reviewer_detail', read_only=True)
    reviewer_url = serializers.ModelSerializer.serializer_url_field(view_name='reviewer_detail')
    class Meta:
        model = Reviewer
        fields = ('id', 'reviewer', 'reviewer_url', 'name')

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedRelatedField(view_name='movie_detail', read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        source='movie'
    )
    reviewer = serializers.HyperlinkedRelatedField(view_name='reviewer_detail', read_only=True)
    reviewer_id = serializers.PrimaryKeyRelatedField(
        queryset=Reviewer.objects.all(),
        source='reviewer'
    )
    class Meta:
        model = Rating
        fields = ('id', 'movie', 'movie_id', 'reviewer', 'reviewer_id', 'review_stars', 'num_o_ratings')

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.HyperlinkedRelatedField(view_name='director_detail', read_only=True)
    director_url = serializers.ModelSerializer.serializer_url_field(view_name='director_detail')

    class Meta:
        model = Director
        fields = ('id', 'director', 'director_url', 'fname', 'lname')

class MovieDirectionSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedRelatedField(view_name='movie_detail', read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        source='movie'
    )
    director = serializers.HyperlinkedRelatedField(view_name='director_detail', read_only=True)
    director_id = serializers.PrimaryKeyRelatedField(
        queryset=Director.objects.all(),
        source='director'
    )
    class Meta:
        model = MovieDirection
        fields = ('id', 'movie', 'movie_id', 'director', 'director_id')