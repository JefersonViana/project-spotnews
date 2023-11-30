from django.urls import path
from .views import homepage, news_detail

urlpatterns = [
    path('', homepage, name='home-page'),
    path('news/<int:id>', news_detail, name='news-details-page'),
]
