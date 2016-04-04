from django import forms
from .models import Post
from .models import Project

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'content', 'image', 'description', 'credits', 'created_date',)
        