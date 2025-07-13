from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):
    categories = Catagory.objects.all()
    first_news = []
    for category in categories:
        category_first_post = News.objects.filter(category=category).order_by('-created_at').first()
        if category_first_post is not None:
            first_news.append(category_first_post)
    first_news = first_news[-5:]
    news = News.objects.order_by('-created_at')
    return render(request, 'index.html', {'categories':categories, 'first_news':first_news, 'news':news})

@login_required(login_url='login')
def category(request, pk):
    category = Catagory.objects.get(id=pk)
    news = News.objects.filter(category=category).order_by('-id')
    print(news)
    return render(request, 'category-01.html', {'news':news})

def new_detail(request, pk):
    post = News.objects.get(id=pk)
    return render(request, 'blog-detail-01.html', {'post':post})
# Create your views here.
