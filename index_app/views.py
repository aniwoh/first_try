from django.shortcuts import render, redirect
from django.http import HttpResponse
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

def orm(request):
    from index_app.models import StudentInfo
    data_list = StudentInfo.objects.filter(name='Clark')
    return HttpResponse([[i.name, i.height, i.weight, i.age] for i in data_list])

def test(request):
    return render(request,'test/test.html')

def test1(request):
    return render(request,'test/siderbar2.html')
