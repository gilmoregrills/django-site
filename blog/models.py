from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
        
class Media(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=200)#is there something that will take an embeddable URL? CharField (must have embed tags) that feeds into the media_item.html
    description = models.CharField(max_length=300)
    credits = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)