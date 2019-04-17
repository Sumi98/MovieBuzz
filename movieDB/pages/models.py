from django.db import models

# Create your models here.


class Movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    rank = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True)
    duration = models.IntegerField(blank=True, null=True)
    genres = models.CharField(max_length=100)
    rating = models.FloatField(blank=True, null=True)
    metascore = models.CharField(max_length=10, default='0')
    votes = models.IntegerField(blank=True, null=True)
    gross_earning_in_mil = models.CharField(max_length=10, default='0')
    director = models.ForeignKey('Director', related_name='+', on_delete=models.CASCADE, null=True, blank=True)
    actor = models.CharField(max_length=30)


class Director(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    date = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=500, null=True)
    masterpiece = models.CharField(max_length=500, null=True)
    award_win = models.IntegerField(blank=True, null=True, default=None)
    award_nom = models.IntegerField(blank=True, null=True, default=None)

class Actor(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    date = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=500, null=True)
    masterpiece = models.CharField(max_length=500, null=True)
    award_win = models.IntegerField(blank=True, null=True, default=None)
    award_nom = models.IntegerField(blank=True, null=True, default=None)
    person_link = models.CharField(max_length=500, null=True)
    award_link = models.CharField(max_length=500, null=True)