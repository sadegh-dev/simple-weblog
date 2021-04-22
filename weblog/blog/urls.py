from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles),
    path('<int:id>/<slug:slug>', views.the_article, name = "the_article"),
]
