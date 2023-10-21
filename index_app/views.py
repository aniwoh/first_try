from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MarkdownFilePool
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

def post(request):
    now_id=request.GET.get('id')
    if not now_id:
        now_id=1
        return redirect(reverse('post') + '?id=1')
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
    return render(request, 'index/post.html', context)

def index(request):
    username = request.COOKIES.get('username', 'Guest')
    posts = MarkdownFilePool.objects.all()
    # for post in posts:
    #     response = requests.get("https://api.baka.fun/acgpic/?rand=289")
    #     if response.status_code == 200:
    #         print(response.text)
    #         post['background_image'] = response.json()['url']
    #     else:
    #         continue
    context = {
        'username': username,
        'posts':posts,
    }
    return render(request, 'index/index.html', context)

def proxy_api(request):
    # 构建API请求的URL
    api_url = "https://www.dmoe.cc/random.php"
    
    # 向API服务器发起请求
    response = requests.get(api_url)
    
    # 检查请求是否成功
    if response.status_code == 200:
        # 获取API响应的二进制内容
        image_data = response.content
        
        # 创建HTTP响应对象，将图像数据作为响应内容
        response = HttpResponse(image_data, content_type="image/jpeg")

          # 设置文件名以触发浏览器下载
        response['Content-Disposition'] = 'attachment; filename="random_image.jpg"'  # 可以更改文件名
        
        return response
    else:
        # 如果请求失败，返回适当的错误
        return JsonResponse({'error': 'API request failed'}, status=500)