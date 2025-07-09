from django.shortcuts import render
from .models import *
def index(request):
    categories = Catagory.objects.all()
    return render(request, 'index.html', {'categories':categories})

# Create your views here.
