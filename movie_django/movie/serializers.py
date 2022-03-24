from rest_framework import serializers
# from .models import 

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = 
        fields = ()

class MovieCastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = 
        fields = ()

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = 
        fields = ()

class MovieGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = 
        fields = ()

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = 
        fields = ()

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = 
        fields = ()

class ReviewerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = 
        fields = ()

class MovieDirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = 
        fields = ()

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = 
        fields = ()