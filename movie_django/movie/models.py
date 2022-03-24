from django.db import models

# Create your models here.

# actor model
class Actor(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.fname

# movie_cast model

# movie model

# movie_genre model

# genre model

# rating model

# reviewer model

# movie_direction model

# director model
