from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MarkdownFilePool
# Create your views here.

def index(request):
    return render(request, "index.html")

def search(request):
    # 1. 查看request的方法和类型
    print(request.method)
    # 2. 接受并输出URL传过来的信息
    print(request.GET)
    # 相应有好几种：
    # 1.
    # return HttpResponse("!")
    # 2.
    # return render(request, "AskAndAns.html")
    # 3.重定向
    return redirect(r"https://cn.bing.com/")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == "aniwoh" and password == "mz321084":
        return HttpResponse("登录成功！！")
    return render(request, "login.html", {"error_msg": "用户名或密码错误"})

def test(request):
    return render(request,'test/test.html')

def test1(request):
    markdown = MarkdownFilePool.objects.first()  # 获取第一个Markdown文件
    return render(request, 'test/siderbar2.html', {'markdown': markdown})

def upload_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        markdown_file = request.FILES['markdown_file']
        
        # 将Markdown内容读取并存储到数据库
        content = markdown_file.read().decode('utf-8')
        markdown = MarkdownFilePool(title=title, content=content, author=author)
        markdown.save()
        
        return redirect('/test1')
    
    return render(request, 'upload.html')
