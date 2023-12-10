from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MarkdownFilePool
from django.urls import reverse
from django.http import JsonResponse
import requests

def post(request):
    now_id=request.GET.get('id')
    if not now_id:
        now_id=1
        return redirect(reverse('post') + '?id=1')
    markdown = MarkdownFilePool.objects.get(id=now_id)  # 获取第一个Markdown文件
    prev_record = MarkdownFilePool.objects.filter(id__lt=markdown.id).last()
    next_record = MarkdownFilePool.objects.filter(id__gt=markdown.id).first()
    
    context = {
        'markdown': markdown,
        'prev_record': prev_record,
        'next_record': next_record,
    }
    return render(request, 'index/post.html', context)

def index(request):
    posts = MarkdownFilePool.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'index/index.html', context)

def proxy_api(request):
    # 构建API请求的URL，要求该api返回的结果是一个图片
    api_url = "https://t.mwm.moe/pc"
    response = requests.get(api_url)
    # 检查请求是否成功
    if response.status_code == 200:
        image_data = response.content
        response = HttpResponse(image_data, content_type="image/jpeg")
        response['Content-Disposition'] = 'attachment; filename="random_image.jpg"'
        return response
    else:
        return JsonResponse({'error': 'API request failed'}, status=500)