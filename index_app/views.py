from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import MarkdownFilePool
from index_app.models import Comments
from index_app.models import Tag
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
        'tags':markdown.tags.all(),
    }
    return render(request, 'index/post.html', context)

def index(request):
    posts = MarkdownFilePool.objects.all()
    tags = Tag.objects.all()
    tag_data = [{'title': tag.name, 'id': tag.id} for tag in tags]
    context = {
        'posts':posts,
        'tags':Tag.objects.all(),
        'tag_data':tag_data,
    }
    return render(request, 'index/index.html', context)

def category(request):
    context = {
    }
    return render(request, 'index/category.html',context)

def filter_articles(request):
    tag_id=request.GET.get('tag_id')
    if int(tag_id) >= 0:
        tag=Tag.objects.get(id=tag_id)
        articles=tag.markdownfilepool_set.all()
    elif int(tag_id) == -1:
        articles=MarkdownFilePool.objects.all()
    elif int(tag_id) == -2:
        articles=MarkdownFilePool.objects.all().order_by('-thumbs_up')
    elif int(tag_id) == -3:
        articles=MarkdownFilePool.objects.all().order_by('-view_count')
    else:
        articles=MarkdownFilePool.objects.all()
    return render(request,'index/filter_articles.html',{'posts':articles})

@login_required
def post_comment(request):
    if request.method == 'POST':
        content=request.POST['text']
        article_id=request.POST['now-article']
        author=request.user.username
        belong_to_comment=request.POST.get('belong_to_comment',0)
        repeatSomeone=request.POST.get('repeatSomeone','')
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

def like_article(request):
    article_id=request.POST.get('article_id')
    markdown=MarkdownFilePool.objects.get(id=article_id)
    markdown.thumbs_up+=1
    markdown.save()
    return JsonResponse({'status':'success','thumbs_up':markdown.thumbs_up})

def dislike_article(request):
    article_id=request.POST.get('article_id')
    markdown=MarkdownFilePool.objects.get(id=article_id)
    markdown.thumbs_up-=1
    markdown.save()
    return JsonResponse({'status':'success','thumbs_up':markdown.thumbs_up})