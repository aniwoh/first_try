from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MarkdownFilePool

def index(request):
    now_id=request.GET.get('id')
    if not now_id:
        now_id=1
    markdown = MarkdownFilePool.objects.get(id=now_id)  # 获取第一个Markdown文件
    prev_record = MarkdownFilePool.objects.filter(id__lt=markdown.id).last()
    next_record = MarkdownFilePool.objects.filter(id__gt=markdown.id).first()
    
    username = request.COOKIES.get('username', 'Guest')
    context = {
        'username': username,
        'markdown': markdown,
        'prev_record': prev_record,
        'next_record': next_record,
    }
    return render(request, 'index/index.html', context)

def post(request):
    username = request.COOKIES.get('username', 'Guest')
    context = {
        'username': username,
    }
    return render(request, 'index/post.html', context)


