from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from index_app.models import MarkdownFilePool
from django.http import JsonResponse
import json
from django.contrib.auth import get_user_model

User = get_user_model()

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
def userall(request):
    users=User.objects.all().values('username','is_superuser','date_joined')
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'userall',
        'users':users
    }
    return render(request,'homepage/userall.html',content)

@login_required
def setting(request):
    username = request.COOKIES.get('username')
    content={
        'username':username,
        'current_page':'setting',
    }
    return render(request,'homepage/setting.html',content)

@login_required
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

@login_required
def get_user_json_api(request):
    users=User.objects.all().values('username','is_superuser','date_joined','id')
    level = users.userprofile.level
    print(level)
    users_list=[]
    for i in users:
        i['date_joined']=i['date_joined'].strftime('%Y-%m-%d %H:%M:%S')
        users_list.append(i)
    user_dict={'code':0,'msg':'','count':len(users),'data':users_list}
    # user_json_data = json.dumps(user_dict)
    return JsonResponse(user_dict)
