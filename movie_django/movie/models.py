from django.db import models

# Create your models here.

# actor model
class Actor(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.fname

# movie model
class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    time = models.IntegerField()
    language = models.CharField(max_length=50)
    release_date = models.DateField(auto_now_add=True)
    release_country = models.CharField(max_length=5)

    def __str__(self):
        return self.title

# movie_cast model
class MovieCast(models.model):
    role = models.CharField(max_length=30)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='movie_cast')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')

    def __str__(self):
        return self.role

# movie_genre model

# genre model

# rating model

# reviewer model

# movie_direction model

# director model
