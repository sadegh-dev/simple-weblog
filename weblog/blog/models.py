from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    
    STATUS = (
        ('d','draft'),
        ('p','publish')
    )
    title = models.CharField(max_length = 120)
    slug = models.SlugField(max_length = 120, unique= True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='d')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('the_article', args=[self.id, self.slug])


