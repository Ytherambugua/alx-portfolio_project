from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Category
from .forms import BlogPostForm

def index(request):
    posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    post.delete()
    return redirect('index')

