from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MarkdownFilePool
import json

def index(request):
    markdown = MarkdownFilePool.objects.first()  # 获取第一个Markdown文件
    next_record_id = request.GET.get('next_record_id')
    prev_record_id = request.GET.get('prev_record_id')
    if next_record_id:
        markdown = MarkdownFilePool.objects.filter(id=next_record_id).first()
    elif prev_record_id:
        markdown = MarkdownFilePool.objects.filter(id=prev_record_id).first()
    
    prev_record = MarkdownFilePool.objects.filter(id__lt=markdown.id).last()
    next_record = MarkdownFilePool.objects.filter(id__gt=markdown.id).first()
    
    username = request.COOKIES.get('username', 'Guest')
    context = {
        'username': username,
        'markdown': markdown,
        'prev_record': prev_record,
        'next_record': next_record,
    }
    return render(request, 'index.html', context)


