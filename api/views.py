from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from django.http import HttpResponse, JsonResponse
from index_app.models import Comments, MarkdownFilePool, Tag
from django.contrib.auth import get_user_model
import json
from django.forms import model_to_dict
from datetime import date, datetime
User = get_user_model()

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def getAllArticles(request):
    return get_article(-1)

def getArticleById(request):
    article_id=request.GET.get('id')
    article =MarkdownFilePool.objects.get(id=article_id)
    articleDict=model_to_dict(article)
    articleDict['created_at'] = article.created_at.strftime('%Y-%m-%d %H:%M:%S')
    articleDict['tags'] = [i.name for i in articleDict['tags']]
    data={'code':0,'msg':'','data':articleDict}
    return JsonResponse(data)

@login_required
def likeComment(request):
    comment_id=json.loads(request.body).get('comment_id')
    comment=Comments.objects.get(id=comment_id)
    comment.thumbs_up+=1
    comment.save()
    return JsonResponse({'status':'success','thumbs_up':comment.thumbs_up})

@login_required
def dislikeComment(request):
    comment_id=json.loads(request.body).get('comment_id')
    comment=Comments.objects.get(id=comment_id)
    comment.thumbs_up-=1
    comment.save()
    return JsonResponse({'status':'success','thumbs_up':comment.thumbs_up})

@login_required
def likeArticle(request):
    article_id=json.loads(request.body).get('article_id')
    print(article_id)
    markdown=MarkdownFilePool.objects.get(id=int(article_id))
    markdown.thumbs_up+=1
    markdown.save()
    return JsonResponse({'status':'success','thumbs_up':markdown.thumbs_up})

@login_required
def dislikeArticle(request):
    article_id=json.loads(request.body).get('article_id')
    markdown=MarkdownFilePool.objects.get(id=int(article_id))
    markdown.thumbs_up-=1
    markdown.save()
    return JsonResponse({'status':'success','thumbs_up':markdown.thumbs_up})

def getAllTags(request):
    tags=Tag.objects.all().values('name','id')
    tags_list=[]
    for i in tags:
        i['title']=i['name']
        i.pop('name')
        tags_list.append(i)
    data={'code':0,'msg':'','data':tags_list}
    return JsonResponse(data)

def filterArticles(request):
    tag_id=request.GET.get('tag_id')
    return get_article(tag_id)

def searchArticles(request):
    keyword=request.GET.get('keyword')
    articles=MarkdownFilePool.objects.filter(title__contains=keyword).values('title','id','view_count','thumbs_up','comment_count','created_at','author','tags__name')
    article_list=articleHelper(articles)
    data={'code':0,'msg':'','data':article_list}
    return JsonResponse(data)

@login_required
def getAllUserByLevel(request):
    current_user_level = request.user.level
    if current_user_level==6: # 为超级管理员
        users=User.objects.all().values('username','is_superuser','date_joined','id','level')
    else:
        users=User.objects.filter(username=request.user.username).values('username','is_superuser','date_joined','id','level')
    users_list=[]
    for i in users:
        i['date_joined']=i['date_joined'].strftime('%Y-%m-%d %H:%M:%S')
        i['level']=replace_level(i['level'])
        users_list.append(i)
    user_dict={'code':0,'msg':'','count':len(users),'data':users_list}
    return JsonResponse(user_dict)

@login_required
def delete_user(request):
    user_id = request.POST['id']
    User.objects.filter(id=user_id).delete()
    return JsonResponse({'status':'success'})


def api_get_iframe(request,filename):
    if request.method == 'GET':
        return render(request,'iframe/'+filename)
    else:
        return JsonResponse({'error':'Method not allowed'},status=405)
    
# 以下写工具
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

def get_article(tag_id):
    if int(tag_id) >= 0:
        tag=Tag.objects.get(id=tag_id)
        articles=tag.markdownfilepool_set.all()
    elif int(tag_id) == -1:
        articles=MarkdownFilePool.objects.all()
    elif int(tag_id) == -2:
        articles=MarkdownFilePool.objects.all().order_by('-thumbs_up')
    elif int(tag_id) == -3:
        articles=MarkdownFilePool.objects.all().order_by('-view_count')
    elif int(tag_id) == -4:
        articles=MarkdownFilePool.objects.all().order_by('-comment_count')
    else:
        articles=MarkdownFilePool.objects.all()
    articles =articles.values('title','id','view_count','thumbs_up','comment_count','created_at','author','tags__name')
    article_list=articleHelper(articles)
    data={'code':0,'msg':'','data':article_list}
    return JsonResponse(data)

def articleHelper(articles):
    article_list=[]
    flag = True
    for i in articles:
        tag_list=[i['tags__name']]
        i['tags__name']=[i['tags__name']]
        for j in article_list:
            if j['id']==i['id']:
                j['tags__name'].append(tag_list[0])
                flag=False
        if flag:
            article_list.append(i)
        flag = True
    return article_list