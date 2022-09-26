from django.shortcuts import render, HttpResponse, Http404
from main.models import Film, Review
from datetime import datetime

# Create your views here.

def about_us(request):
    return render(request, 'about_us.html')

def date_now(request):
    return render(request, 'date_now.html')


def film_list_view(request):
    film_list = Film.objects.all()
    context = {
        'film_list': film_list
    }

    return render(request, 'film.html', context=context)


def film_item_view(request, id):
    try:
        film_list = Film.objects.get(id=id)
    except Film.DoesNotExist:
        raise Http404 ('Film not found')
    context = {
        'film_detail': film_list,
        'reviews': Review.objects.filter(film_id = id)
    }
    return render(request, 'detail.html', context=context)