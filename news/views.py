from django.shortcuts import render
from .models import News


def homepage(request):
    context = {"news": News.objects.all(), "title": "Trybe News"}
    return render(request, 'home.html', context)


def news_detail(request, id):
    context = {"new": News.objects.get(id=id)}
    return render(request, 'news_details.html', context)
