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
class MovieCast(models.Model):
    role = models.CharField(max_length=30)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='movie_cast')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')

    def __str__(self):
        return self.role

# genre model
class Genre(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

# movie_genre model
class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre')

    def __str__(self):
        return self.genre

# reviewer model
class Reviewer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# rating model
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='reviewer')
    review_stars = models.IntegerField()
    num_o_ratings = models.IntegerField()

    def __str__(self):
        return self.review_stars

# director model
class Director(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.fname} {self.lname}'

# movie_direction model
class MovieDirection(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director')

    def __str__(self):
        return self.director