from django import forms
from .models import Post
from .models import Media

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)
        
class MediaForm(forms.ModelForm):
    
    class Meta:
        model = Media
        fields = ('title', 'content', 'description', 'credits')