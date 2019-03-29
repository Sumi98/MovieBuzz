from django.shortcuts import render
from .models import Movie
import csv

# Create your views here.
# def whole_list(request, model, page):
#     # if page is None:
#     #     return render(request, '404.html')
#     page = int(page)
#     objects = model.objects.all()
#     total_page = int(math.ceil(len(objects) / 10))
#     # if page > total_page:
#     #     return render(request, '404.html')
#     last_item_index = 10 * page if page != total_page else len(objects)
#     pages = []
#     end_distance = total_page - page
#     start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
#     end_page_num = page + 5 if page > 5 else 10
#     for i in range(start_page_num, end_page_num + 1):
#         if 1 <= i <= total_page:
#             pages.append(i)
#     data = {'items': objects[10 * (page - 1):last_item_index], 'current_page': page, 'page_number': total_page,
#             'pages': pages}
#     return render(request, '{}_list.html'.format(model.get_name()), data)


def home(request):
	return render(request, "home.html", {})


def movie(request):

	with open(r'/Users/andy/PycharmProjects/CS411_Project/Data/movie_data_0325.csv') as f:
		reader = csv.DictReader(f)
		for line in reader:
			tmp = Movie(movieid=line['Movie_ID'], year=line['Year'], rank=line['Rank'], title=line['Title'],
						description=line['Description'], duration=line['Duration'], genres=line['Genre'],
						rating=line['Rating'], metascore=line['Metascore'], votes=line['Votes'],
						gross_earning_in_mil=line['Gross_Earning_in_Mil'], director=line['Director'],
						actor=line['Actor'])

			tmp.save()
	return render(request, "movie.html", {})


def director(request):
	return render(request, "director.html", {})


def actor(request):
	return render(request, "actor.html", {})


def prediction(request):
	return render(request, "prediction.html", {})


def recommendation(request):
	return render(request, "recommendation.html", {})


def insert_data(request):
	return render(request, "insert_data.html", {})


def insert_data_submission(request):
	print('New Movie Submitted!')
	year = request.POST["year"]
	title = request.POST["title"]
	genres = request.POST["type"]
	director_name = request.POST["director"]
	actor_name = request.POST.get("actor", False)

	new_movie = Movie(title=title, year=year, genres=genres, director=director_name, actor=actor_name)
	new_movie.save()
	return render(request, "insert_data.html", {})
