from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def homepage(request):
    username = request.COOKIES.get('username')
    content={
        'username':username
    }
    return render(request,'homepage.html',content)

def home(request):
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'home',
    }
    return render(request,'homepage/home.html',content)

def list(request):
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'list',
    }
    return render(request,'homepage/list.html',content)

def data(request):
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'data',
    }
    return render(request,'homepage/data.html',content)

def plugin(request):
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'plugin',
    }
    return render(request,'homepage/plugin.html',content)

def setting(request):
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'setting',
    }
    return render(request,'homepage/setting.html',content)