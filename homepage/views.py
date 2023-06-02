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
