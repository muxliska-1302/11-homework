from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.all()
    ctx = {'posts':posts}
    return render(request, 'index.html', ctx)

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        author = request.POST.get('author')
        if title and category and short_content and long_content and author:
            Post.objects.create(
                title = title,
                category = category,
                short_content = short_content,
                long_content = long_content,
                author = author
            )
            return redirect('home')
    return render(request,'news/add-news.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    ctx = {'post':post}
    return render(request, 'news/detail.html', ctx)

def post_by_category(request, category):
    posts = Post.objects.filter(category=category)
    ctx = {'posts':posts, 'category':category}
    return render(request, 'news/news-by-category.html', ctx)