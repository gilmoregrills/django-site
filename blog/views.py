from django.shortcuts import render
from django.utils import timezone 
from .models import Post
from .models import Project
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ProjectForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form' : form})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'blog/project_detail.html', {'project' : project})

def project_list(request):
    projects = Project.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/project_list.html', {'projects' : projects})

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST,)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.created_date = timezone.now()
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'blog/project_edit.html', {'form' : form})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project) 
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.created_date = timezone.now()
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'blog/project_edit.html', {'form' : form})