from django.shortcuts import render, redirect
from .models import News
from .forms import CreateNewsModelForm


def homepage(request):
    context = {"news": News.objects.all(), "title": "Trybe News"}
    return render(request, 'home.html', context)


def news_detail(request, id):
    context = {"new": News.objects.get(id=id)}
    return render(request, 'news_details.html', context)


def create_news(request):
    if request.method == 'POST':
        form = CreateNewsModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    form = CreateNewsModelForm()
    return render(request, 'categories_form.html', {'form': form})
