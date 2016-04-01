from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Media

admin.site.register(Media)
admin.site.register(Post)   