from django.shortcuts import render
from django.template.defaulttags import comment

from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    categories = Catagory.objects.all()
    first_news = []
    for category in categories:
        category_first_post = News.objects.filter(category=category).order_by('-created_at').first()
        if category_first_post is not None:
            first_news.append(category_first_post)
    first_news = first_news[-4:]
    news = News.objects.order_by('-created_at')
    return render(request, 'index.html', {'categories':categories, 'first_news':first_news, 'news':news})

@login_required(login_url='login')
def category(request, pk):
    category = Catagory.objects.get(id=pk)
    news = News.objects.filter(category=category).order_by('-id')
    categories = Catagory.objects.all()
    return render(request, 'category-01.html', {'news':news, 'categories':categories})

def new_detail(request, pk):
    post = News.objects.get(id=pk)
    comments = Comment.objects.filter(news=post).order_by('-id')[:3]
    if request.method == "POST":
        comment = request.POST['msg']
        Comment.objects.create(
            news = post,
            pos_text = comment,
            user = request.user
        )
        print(comment)
        messages.info(request, 'Comment qoldirdingiz')

    return render(request, 'blog-detail-01.html', {'post':post, 'comments':comments})
# Create your views here.
@login_required
def profile(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'account/profile.html', {'user':user})