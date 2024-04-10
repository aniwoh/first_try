from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from index_app.models import MarkdownFilePool,Tag
from django.http import JsonResponse
import json
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

@login_required
def home(request):
    content={
        'current_page':'home',
    }
    return render(request,'homepage/home.html',content)

@login_required
def list(request):
    posts = MarkdownFilePool.objects.all()
    tags = Tag.objects.all()
    content={
        'current_page':'list',
        'posts':posts,
        'tags':tags,
    }
    return render(request,'homepage/list.html',content)

@login_required
def data(request):
    content={
        'current_page':'data',
    }
    return render(request,'homepage/data.html',content)

@login_required
def userall(request):
    users=User.objects.all().values('username','is_superuser','date_joined')
    content={
        'current_page':'userall',
        'users':users
    }
    return render(request,'homepage/userall.html',content)

@login_required
def setting(request):
    content={
        'current_page':'setting',
    }
    return render(request,'homepage/setting.html',content)

@login_required
def upload_view(request):
    if request.method == 'POST':
        print(request.POST)
        tags= request.POST.getlist('tags',[])
        temp_list=[]
        for i in tags:
            if not i.isdigit():
                Tag.objects.create(name=i)
                tag_id = Tag.objects.get(name=i).id
                temp_list.append(tag_id)
            else: # 是纯数字
                if Tag.objects.filter(id=i).exists():
                    temp_list.append(i)
                else:
                    continue
        tags=temp_list
        title = request.POST['title']
        author = request.user.username
        markdown_file = request.FILES['file']
        # 将Markdown内容读取并存储到数据库
        content = markdown_file.read().decode('utf-8')
        markdown = MarkdownFilePool(title=title, content=content, author=author)
        markdown.save()
        for tag_id in tags:
            markdown.tags.add(tag_id)
        return redirect('/homepage/list')
    elif request.method == 'GET':
        print('GET')
        return render(request,'homepage/upload.html')
    
    return redirect('/homepage/list')

@login_required
def get_markdown_json_api(request):
    current_user_level = request.user.level
    if current_user_level==6: # 为超级管理员
        markdown=MarkdownFilePool.objects.all().values('id','title','author','content','created_at','comment_count','view_count','thumbs_up')
    else:
        markdown=MarkdownFilePool.objects.filter(author=request.user.username).values('id','title','author','content','created_at','comment_count','view_count','thumbs_up')
    markdown_list=[]
    for i in markdown:
        i['created_at']=i['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        markdown=MarkdownFilePool.objects.filter(id=i['id']).values('tags')
        tag_list=[]
        for j in markdown:
            if j['tags']== None:
                tag_name='无标签'
            else:
                tag_name=Tag.objects.filter(id=j['tags']).values('name')[0]['name']
            tag_list.append(tag_name)
        i['tags']=tag_list
        markdown_list.append(i)
    markdown_dict={'code':0,'msg':'','count':len(markdown),'data':markdown_list}
    # user_json_data = json.dumps(user_dict)
    return JsonResponse(markdown_dict)

@login_required
def delete_article(request):
    print(request.POST['id'])
    article_id = request.POST['id']
    MarkdownFilePool.objects.filter(id=article_id).delete()
    return redirect('/homepage/list')

@login_required
def edit(request):
    data_id = request.GET['id']
    post=MarkdownFilePool.objects.filter(id=data_id)
    tags = Tag.objects.all()
    content={
        'data_id':data_id,
        'tags':tags,
        'post':post,
    }
    return render(request,'homepage/edit.html',content)