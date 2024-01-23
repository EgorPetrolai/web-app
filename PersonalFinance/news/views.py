
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
def news_home (request):
    news = Article.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


@login_required
def add_new_news(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('news_home')  # Измените на вашу домашнюю страницу новостей
    else:
        form = ArticleForm()

    return render(request, 'news/add_new_news.html', {'form': form})