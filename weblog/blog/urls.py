from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.articles, name='home'),
    path('<int:id>/<slug:slug>', views.the_article, name="the_article"),
]
