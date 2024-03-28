from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import MarkdownFilePool
from index_app.models import Comments
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
import requests
import datetime

def post(request):
    now_id=request.GET.get('id')
    if not now_id:
        now_id=1
        return redirect(reverse('post') + '?id=1')
    markdown = MarkdownFilePool.objects.get(id=now_id)  # 获取第一个Markdown文件
    prev_record = MarkdownFilePool.objects.filter(id__lt=markdown.id).last()
    next_record = MarkdownFilePool.objects.filter(id__gt=markdown.id).first()

    markdown.view_count+=1
    markdown.save()
    
    root_comments=Comments.objects.filter(article_id=now_id,belong_to_comment=0)
    child_comments=Comments.objects.filter(article_id=now_id,belong_to_comment__gt=0)
    context = {
        'markdown': markdown,
        'prev_record': prev_record,
        'next_record': next_record,
        'root_comments':root_comments,
        'child_comments':child_comments,
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

@login_required
def post_comment(request):
    if request.method == 'POST':
        content=request.POST['text']
        article_id=request.POST['now-article']
        author=request.user.username
        belong_to_comment=request.POST['belong_to_comment']
        repeatSomeone=request.POST['repeatSomeone']
        comment=Comments(content=content,article_id=article_id,author=author,belong_to_comment=belong_to_comment,repeat_someone=repeatSomeone)
        print(comment)
        comment.save()
        return redirect(f'/index/post?id={article_id}')

def format_date(date):
    return date.strftime("%Y-%m-%d")

def like_comment(request):
    comment_id=request.POST.get('comment_id')
    comment=Comments.objects.get(id=comment_id)
    comment.thumbs_up+=1
    comment.save()
    return JsonResponse({'status':'success','thumbs_up':comment.thumbs_up})

def dislike_comment(request):
    comment_id=request.POST.get('comment_id')
    comment=Comments.objects.get(id=comment_id)
    comment.thumbs_up-=1
    comment.save()
    return JsonResponse({'status':'success','thumbs_up':comment.thumbs_up})