from django.urls import path
from .views import homepage, news_detail, create_news

urlpatterns = [
    path('', homepage, name='home-page'),
    path('news/<int:id>', news_detail, name='news-details-page'),
    path('categories', create_news, name='categories-form'),
]
