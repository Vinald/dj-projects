from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_articles, name='article_home'),
]