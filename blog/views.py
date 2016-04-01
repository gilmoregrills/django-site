from django.shortcuts import render
from django.utils import timezone 
from .models import Post
from .models import Media
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import MediaForm
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

def media_detail(request, pk):
    media = get_object_or_404(Media, pk=pk)
    return render(request, 'blog/media_detail.html', {'media' : media})

def media_list(request):
    medias = Media.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/media_list.html', {'medias' : medias})

def media_new(request):
    if request.method == "POST":
        form = MediaForm(request.POST)
        if form.is_valid():
            media = form.save(commit=False)
            media.author = request.user
            media.created_date = timezone.now()
            media.save()
            return redirect('media_detail', pk=media.pk)
    else:
        form = MediaForm()
    return render(request, 'blog/media_edit.html', {'form' : form})

def media_edit(request, pk):
    media = get_object_or_404(Media, pk=pk)
    if request.method == "POST":
        form = MediaForm(request.POST, instance=media) 
        if form.is_valid():
            media = form.save(commit=False)
            media.author = request.user
            media.created_date = timezone.now()
            media.save()
            return redirect('media_detail', pk=media.pk)
    else:
        form = MediaForm(instance=media)
    return render(request, 'blog/media_edit.html', {'form' : form})