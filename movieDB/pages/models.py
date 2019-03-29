from django.db import models

# Create your models here.


class Movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    rank = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    duration = models.IntegerField(blank=True, null=True)
    genres = models.CharField(max_length=100)
    rating = models.FloatField(blank=True, null=True)
    metascore = models.CharField(max_length=10, default='0')
    votes = models.IntegerField(blank=True, null=True)
    gross_earning_in_mil = models.CharField(max_length=10, default='0')
    director = models.CharField(max_length=30)
    actor = models.CharField(max_length=30)
    # poster = models.URLField(default='')
    # trailer = models.URLField(default='')

    # def __str__(self):
    #     return self.movieid + '|' + self.title
    #
    # @staticmethod
    # def get_name():
    #     return 'movie'