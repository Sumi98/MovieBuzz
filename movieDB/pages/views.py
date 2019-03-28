from django.shortcuts import render

# Create your views here.
def whole_list(request, model, page):
    # if page is None:
    #     return render(request, '404.html')
    page = int(page)
    objects = model.objects.all()
    total_page = int(math.ceil(len(objects) / 10))
    # if page > total_page:
    #     return render(request, '404.html')
    last_item_index = 10 * page if page != total_page else len(objects)
    pages = []
    end_distance = total_page - page
    start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
    end_page_num = page + 5 if page > 5 else 10
    for i in range(start_page_num, end_page_num + 1):
        if 1 <= i <= total_page:
            pages.append(i)
    data = {'items': objects[10 * (page - 1):last_item_index], 'current_page': page, 'page_number': total_page,
            'pages': pages}
    return render(request, '{}_list.html'.format(model.get_name()), data)

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