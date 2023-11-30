from django.shortcuts import render
from .models import News


def homepage(request):
    context = {"news": News.objects.all(), "title": "Trybe News"}
    return render(request, 'home.html', context)
