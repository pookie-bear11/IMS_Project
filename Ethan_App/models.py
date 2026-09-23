from django.db import models


class MovieAnime(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    rating = models.FloatField()
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.title