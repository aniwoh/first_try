from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from index_app.models import MarkdownFilePool

@login_required
def home(request):
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'home',
    }
    return render(request,'homepage/home.html',content)

@login_required
def list(request):
    posts = MarkdownFilePool.objects.all()
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'list',
        'posts':posts
    }
    return render(request,'homepage/list.html',content)

@login_required
def data(request):
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'data',
    }
    return render(request,'homepage/data.html',content)

@login_required
def plugin(request):
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'plugin',
    }
    return render(request,'homepage/plugin.html',content)

@login_required
def setting(request):
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'setting',
    }
    return render(request,'homepage/setting.html',content)

def upload_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        markdown_file = request.FILES['markdown_file']
        
        # 将Markdown内容读取并存储到数据库
        content = markdown_file.read().decode('utf-8')
        markdown = MarkdownFilePool(title=title, content=content, author=author)
        markdown.save()
        
        return redirect('/homepage/list')
    
    return redirect('/homepage/list')

