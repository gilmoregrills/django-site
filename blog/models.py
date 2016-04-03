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
    
media = models.ForeignKey('Media')
    
class Media(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    content = models.URLField()#is there something that will take an embeddable URL? CharField (must have embed tags) that feeds into the media_item.html
    image = models.ImageField(upload_to='blog/uploads/images', height_field=400, width_field=400, max_length=100, blank=True,)
    description = models.TextField()
    credits = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title