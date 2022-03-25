from rest_framework import serializers
from .models import Actor, Movie, MovieCast

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
        fields = ()

# class MovieGenreSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = 
#         fields = ()

# class GenreSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = 
#         fields = ()

# class RatingSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = 
#         fields = ()

# class ReviewerSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = 
#         fields = ()

# class MovieDirectionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = 
#         fields = ()

# class DirectorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = 
#         fields = ()