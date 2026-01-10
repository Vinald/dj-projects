from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_articles, name='article_home'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('add/', views.add_article, name='add_article'),
]