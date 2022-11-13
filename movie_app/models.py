from django.db import models
from django.db.models import Avg


class Director(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    duration = models.TimeField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def filter_reviews(self):
        return self.reviews.filter(stars__gt=3)

    @property
    def rating(self):
        return self.reviews.aggregate(avg_rating=Avg('stars'))['avg_rating']




STARS = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *'),
)


class Review(models.Model):
    text = models.TextField(max_length=100)
    stars = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text

    @property
    def movie_str(self):
        return self.movie.title
