from django.shortcuts import render
from .models import Article

def home_articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}  # use a dict, not a set like {articles}
    return render(request, 'articles/home.html', context)