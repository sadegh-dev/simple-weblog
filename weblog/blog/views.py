from django.shortcuts import render
from .models import Article

def articles(request):
    posts = Article.objects.all()
    context = {
        'posts': posts,
    }
    return render (request, 'articles.html', context)