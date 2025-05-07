# hexlet_django_blog/article/views.py
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'app_name': 'Hexlet Django Blog - Article'
    }
    return render(request, 'articles/index.html', context)