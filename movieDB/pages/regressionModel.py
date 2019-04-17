import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()

from pages.models import Movie, Director, Actor
import numpy as np

# def 

def build_lg_model(Movie, Director, Actor):
	all_director = Director.objects.all()
	all_movie = Movie.objects.all()
	all_actor = Actor.objects.all()

	pass

def prediction_box_office():
	pass

# all_director = Director.objects.all()
# all_movie = Movie.objects.all()
# all_actor = Actor.objects.all()

# m_year = list(map(lambda x: int(x.year), Movie.objects.only("year")))
# m_title = list(map(lambda x: x.title, Movie.objects.only("title")))
# m_genre = list(map(lambda x: x.genres, Movie.objects.only("genres")))
# m_rating = list(map(lambda x: float(x.rating), Movie.objects.only("rating")))
# m_metScore= list(map(lambda x: int(x.metascore), Movie.objects.only("metascore")))
# m_votes = list(map(lambda x: int(x.votes), Movie.objects.only("votes")))
# m_earn = list(map(lambda x: float(x.gross_earning_in_mil), Movie.objects.only("gross_earning_in_mil")))
# # arr = np.array([m_earn[:60], m_title[:60]])
# # print(arr)
# print(m_year[:5])