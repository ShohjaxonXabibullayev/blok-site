from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Parollar togri kelmadi')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu username orqali avval royhatdan otilgan')
            return redirect('signup')

        User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
        messages.success(request, 'Siz muvafaqqiyatli royhatdan otdingiz!')
        return redirect('login')

    return render(request, 'account/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username is None or password is None:
            messages.error(request, 'Login yoki parol kiritilmadi')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Siz login qildingiz!')
            return redirect('index')
        messages.error(request, 'Bunaqa user topilmadi')
        return redirect('login')
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Siz dasturdan chiqdingiz')
    return redirect('index')



# Create your views here.
