from django.shortcuts import render, redirect
from .models import Article

def home_articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}  # use a dict, not a set like {articles}
    return render(request, 'articles/home.html', context)


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return redirect('article_home')
    return render(request, 'articles/add_article.html')