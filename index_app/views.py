from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MarkdownFilePool
from index_app.models import Comments
from django.urls import reverse

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
    return render(request, 'index/index.html')

def category(request):
    context = {
    }
    return render(request, 'index/category.html',context)

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
