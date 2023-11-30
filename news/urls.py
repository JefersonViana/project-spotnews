from django.urls import path
from .views import homepage, news_detail, create_categories, create_news

urlpatterns = [
    path('', homepage, name='home-page'),
    path('news/<int:id>', news_detail, name='news-details-page'),
    path('categories', create_categories, name='categories-form'),
    path('news', create_news, name='news-form'),
]
