from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MarkdownFilePool
# Create your views here.

def index(request):
    markdown = MarkdownFilePool.objects.first()  # 获取第一个Markdown文件
    username = request.COOKIES.get('username', 'Guest')
    return render(request, 'index.html', {'markdown': markdown,'username': username})

def test(request):
    return render(request,'test/test.html')

def upload_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        markdown_file = request.FILES['markdown_file']
        
        # 将Markdown内容读取并存储到数据库
        content = markdown_file.read().decode('utf-8')
        markdown = MarkdownFilePool(title=title, content=content, author=author)
        markdown.save()
        
        return redirect('/test1')
    
    return render(request, 'upload.html')


