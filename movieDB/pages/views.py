from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Movie, Director
import csv, os
from .forms import MovieForm
from django.core.paginator import Paginator


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


def director(request):
    base_dir = os.path.abspath(__file__)

    for i in range(3):
        base_dir = os.path.dirname(base_dir)

    with open(base_dir + '/Data/director.csv') as g:
        reader = csv.DictReader(g)
        for line in reader:
            try:
                val = int(line['dr_awards_wins'])
            except ValueError:
                val = None

            try:
                val_nom = int(line['dr_awards_nomi tions'])
            except ValueError:
                val_nom = None

            tmp = Director(name=line['dr_name'], date=line['dr_date'], place=line['dr_place'],
                           masterpiece=line['dr_knownfor'], award_win=val,
                           award_nom=val_nom)

            tmp.save()

    all_director = Director.objects.all()

    paginator = Paginator(all_director, 50)
    page = request.GET.get('page')
    directors = paginator.get_page(page)

    return render(request, "director.html", {'Director': directors})


def movie(request):
    base_dir = os.path.abspath(__file__)

    for i in range(3):
        base_dir = os.path.dirname(base_dir)

    with open(base_dir + '/Data/movie_data_0325.csv') as f:
        reader = csv.DictReader(f)
        for line in reader:

            try:
                director_nm = Director.objects.get(name=line['Director'])
            except Director.DoesNotExist:
                director_nm = None

            tmp = Movie(movieid=line['Movie_ID'], year=line['Year'], rank=line['Rank'], title=line['Title'],
                        description=line['Description'], duration=line['Duration'], genres=line['Genre'],
                        rating=line['Rating'], metascore=line['Metascore'], votes=line['Votes'],
                        gross_earning_in_mil=line['Gross_Earning_in_Mil'], director=director_nm,
                        actor=line['Actor'])

            tmp.save()

    all_movies = Movie.objects.all()

    paginator = Paginator(all_movies, 50)
    page = request.GET.get('page')
    movies = paginator.get_page(page)

    return render(request, "movie.html", {'Movie': movies})


def actor(request):
    return render(request, "actor.html", {})


def prediction(request):
    return render(request, "prediction.html", {})


def recommendation(request):
    return render(request, "recommendation.html", {})


def insert_data(request):
    return render(request, "insert_data.html", {})


def insert_data_submission(request):
    year = request.POST["year"]
    title = request.POST["title"]
    genres = request.POST["type"]
    descrption = request.POST["description"]
    director_name = request.POST["director"]
    actor_name = request.POST.get("actor", False)

    new_movie = Movie(title=title, year=year, genres=genres, description=descrption, director=director_name,
                      actor=actor_name)
    new_movie.save()
    return render(request, "insert_data.html", {})


def edit_movie(request, pk):
    post = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your movie has been updated!')
        except Exception as e:
            messages.warning(request, 'Your movie was not updated: Error {}'.format(e))
    else:
        form = MovieForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, "new_movie.html", context)


def new_movie(request):
    template = 'new_movie.html'
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, template, context)


def delete_movie(request, pk):
    post = get_object_or_404(Movie, pk=pk)
    try:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=post)
            post.delete()
            messages.success(request, 'You have successfully deleted the movie')
        else:
            form = MovieForm(instance=post)
    except Exception as e:
        messages.warning(request, 'The movie cannot be deleted: Error {}'.format(e))
    context = {
        'form': form,
        'post': post
    }
    return render(request, "new_movie.html", context)


def search(request):
    template = 'home.html'

    query = request.GET.get('q')
    tep = "%%%s%%" % query
    filter_title = Director.objects.raw(
        "SELECT m.title AS title, d.name AS name, d.masterpiece AS knownfor FROM pages_director AS d LEFT JOIN movie_0325 AS m ON d.name = m.director WHERE m.title LIKE %s",
        [tep])

    return render(request, template, {'filter_title': filter_title})
