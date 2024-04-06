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
        author = request.user.username
        markdown_file = request.FILES['file']
        # 将Markdown内容读取并存储到数据库
        content = markdown_file.read().decode('utf-8')
        markdown = MarkdownFilePool(title=title, content=content, author=author)
        markdown.save()
        
        return redirect('/homepage/list')
    elif request.method == 'GET':
        print('GET')
        return render(request,'homepage/upload.html')
    
    return redirect('/homepage/list')

@login_required
def get_user_json_api(request):
    users=User.objects.all().values('username','is_superuser','date_joined','id','level')
    users_list=[]
    for i in users:
        i['date_joined']=i['date_joined'].strftime('%Y-%m-%d %H:%M:%S')
        i['level']=replace_level(i['level'])
        users_list.append(i)
    user_dict={'code':0,'msg':'','count':len(users),'data':users_list}
    # user_json_data = json.dumps(user_dict)
    return JsonResponse(user_dict)

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
        markdown_list.append(i)
    markdown_dict={'code':0,'msg':'','count':len(markdown),'data':markdown_list}
    # user_json_data = json.dumps(user_dict)
    return JsonResponse(markdown_dict)

def replace_level(level):
    # 致敬《魔禁》
    if level==0:
        return '无能力者'
    elif level==1:
        return '低能力者'
    elif level==2:
        return '异能力者'
    elif level==3:
        return '强能力者'
    elif level==4:
        return '大能力者'
    elif level==5:
        return '超能力者'
    elif level==6:
        return '绝对能力者'
    else:
        return '魔法士'
    
@login_required
def delete_user(request):
    print(request.POST['id'])
    user_id = request.POST['id']
    User.objects.filter(id=user_id).delete()
    return redirect('/homepage/userall')