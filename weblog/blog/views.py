from django.shortcuts import render, get_object_or_404
from .models import Article

def articles(request):
    posts = Article.objects.all()
    context = {
        'posts': posts,
    }
    return render (request, 'articles.html', context) 


def the_article(request, id, slug):
    #the_post = Article.objects.get(id = id, slug = slug)
    the_post = get_object_or_404(Article, id=id , slug=slug)
    context = {
        'the_post': the_post
    }
    return render(request, 'the_article.html', context)


