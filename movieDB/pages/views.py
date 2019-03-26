from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "home.html", {})

def movie(request):
	return render(request, "movie.html", {})

def director(request):
	return render(request, "director.html", {})

def actor(request):
	return render(request, "actor.html", {})

def prediction(request):
	return render(request, "prediction.html", {})

def recommendation(request):
	return render(request, "recommendation.html", {})