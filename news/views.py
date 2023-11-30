from django.shortcuts import render, redirect
from .models import News
from .forms import CreateCategoriesModelForm, CreateNewsModelForm


def homepage(request):
    context = {"news": News.objects.all(), "title": "Trybe News"}
    return render(request, 'home.html', context)


def news_detail(request, id):
    context = {"new": News.objects.get(id=id)}
    return render(request, 'news_details.html', context)


def create_categories(request):
    if request.method == 'POST':
        form = CreateCategoriesModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    form = CreateCategoriesModelForm()
    return render(request, 'categories_form.html', {'form': form})


def create_news(request):
    if request.method == 'POST':
        form = CreateNewsModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    form = CreateNewsModelForm()
    return render(request, 'news_form.html', {'form': form})
