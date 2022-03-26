from django.contrib import admin
from .models import Actor, Movie, MovieCast, Genre, MovieGenre, Reviewer, Rating, Director, MovieDirection

# Register your models here.
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieCast)
admin.site.register(Genre)
admin.site.register(MovieGenre)
admin.site.register(Reviewer)
admin.site.register(Rating)
admin.site.register(Director)
admin.site.register(MovieDirection)