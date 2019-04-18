import os
import pip
# enable relect results in terminal
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()
from pages.models import Movie, Director, Actor

import numpy as np
import pandas as pd

from scipy import stats
from datetime import datetime
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try:
	import pandasql as ps
except ImportError:
	install('pandasql')

def get_Movie_df(Movie):
	# store records into a dataframe
	movie_df = pd.DataFrame()
	movie_df['Year'] = pd.Series(list(map(lambda x: int(x.year), Movie.objects.only("year"))))
	movie_df['Title'] = pd.Series(list(map(lambda x: x.title, Movie.objects.only("title"))))
	movie_df['Genre'] = pd.Series(list(map(lambda x: x.genres, Movie.objects.only("genres"))))
	movie_df['Rating'] = pd.Series(list(map(lambda x: float(x.rating), Movie.objects.only("rating"))))
	movie_df['MetScore'] = pd.Series(list(map(lambda x: int(x.metascore), Movie.objects.only("metascore"))))
	movie_df['Votes'] = pd.Series(list(map(lambda x: int(x.votes), Movie.objects.only("votes"))))
	movie_df['Earned'] = pd.Series(list(map(lambda x: float(x.gross_earning_in_mil), Movie.objects.only("gross_earning_in_mil"))))
	# Remove the row with 0 (originally None)
	movie_df.replace(0, np.nan, inplace=True)
	movie_df = movie_df.dropna()

	# Convert category variable to indicator variable
	dummy_df = pd.get_dummies(movie_df.Genre, prefix = 'Genre')
	movie_df = movie_df.join(dummy_df)

	return movie_df
	# pass

def get_Actor_df(Actor):
	actor_df = pd.DataFrame()
	actor_df['Name'] = pd.Series(list(map(lambda x: x.name, Actor.objects.only("name"))))
	actor_df['Date'] = pd.Series(list(map(lambda x: x.date, Actor.objects.only("date"))))
	actor_df['Masterpiece'] = pd.Series(list(map(lambda x: x.masterpiece, Actor.objects.only("masterpiece"))))
	actor_df['AwardWin'] = pd.Series(list(map(lambda x: int(x.award_win), Actor.objects.only("award_win"))))
	actor_df['AwardNom'] = pd.Series(list(map(lambda x: int(x.award_nom), Actor.objects.only("award_nom"))))
	# string split by ', ', only key first 4 columns
	masterpiece_tmp = pd.DataFrame(list(map(lambda x: x.masterpiece.split(', '), Actor.objects.only("masterpiece")))).drop([4, 5, 6], axis = 1)
	masterpiece_tmp.columns = ['Masterpiece_1', 'Masterpiece_2', 'Masterpiece_3', 'Masterpiece_4']
	actor_df = actor_df.join(masterpiece_tmp)
	return actor_df
	# pass

def get_Director_df(Director):
	director_df = pd.DataFrame()
	director_df['Name'] = pd.Series(list(map(lambda x: x.name, Director.objects.only("name"))))
	director_df['Date'] = pd.Series(list(map(lambda x: x.date, Director.objects.only("date"))))
	# string split by ', ', only key first 4 columns
	masterpiece_tmp = pd.DataFrame(list(map(lambda x: (x.masterpiece).split(', '), Director.objects.only("masterpiece")))).drop([4, 5], axis = 1)
	masterpiece_tmp.columns = ['Masterpiece_1', 'Masterpiece_2', 'Masterpiece_3', 'Masterpiece_4']
	director_df['AwardWin'] = pd.Series(list(map(lambda x: int(x.award_win), Director.objects.only("award_win"))))
	director_df['AwardNom'] = pd.Series(list(map(lambda x: int(x.award_nom), Director.objects.only("award_nom"))))
	director_df = director_df.join(masterpiece_tmp)
	return director_df
	# pass

def build_lg_model(Movie, Director, Actor):
	movie_df = get_Movie_df(Movie)
	actor_df = get_Actor_df(Actor)
	director_df = get_Director_df(Director)
	print(movie_df.columns)
	print(actor_df.columns)
	print(director_df.columns)

	X = movie_df.drop(['Genre', 'Title', 'Earned'], axis = 1)
	y = movie_df.Earned

	model_lg = LinearRegression()
	scores = []
	kfold = KFold(n_splits=3, shuffle=True, random_state=3)
	for i, (train, test) in enumerate(kfold.split(X, y)):
		model_lg.fit(X.iloc[train,:], y.iloc[train])
		score = model_lg.score(X.iloc[test,:], y.iloc[test])
		scores.append(score)

	# Split X and y into X_
	# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
	return scores
	# pass

def prediction_box_office():
	pass


# movie_df = get_Movie_df(Movie)
# print(movie_df[:5])
# print(pd.get_dummies(movie_df.loc[:5].Genre))
# score = build_lg_model(Movie, Director, Actor)
# print(score)

# actor_df = get_Actor_df(Actor)
# print(actor_df.loc[:5, 'Masterpiece'])

# director_df = get_Director_df(Director)
# print(director_df.iloc[:5])

# SQL v.s. panda
# airport_freq.merge(airports[airports.ident == 'KLAX'][['id']], 
# 				   left_on='airport_ref', 
# 				   right_on='id', 
# 				   how='inner')[['airport_ident', 'type', 'description', 'frequency_mhz']]

# select airport_ident, type, description, frequency_mhz from airport_freq join airports on airport_freq.airport_ref = airports.id where airports.ident = 'KLAX'






