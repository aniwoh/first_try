from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from my_settings import *

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        # 验证用户名密码是否正确，验证成功返回用户对象
        if user is not None:
            login(request, user)
            response = redirect('/index')
            return response  # 登录成功后重定向到主页
        else:
            error_message = "账号或密码错误"
            return render(request, 'login_app/login.html', {'error_message': error_message})
    
    return render(request, 'login_app/login.html')

def register(request):
    if ALLOW_REGISTER:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')  # 注册成功后重定向到首页或其他页面
        else:
            form = UserRegistrationForm()
    else:
        text = "管理员已关闭注册功能"
        response = HttpResponse(text, content_type="text/plain; charset=utf-8")
        return response
    
    # error_message = form.errors.as_data()
    return render(request, 'login_app/register.html', {'form': form})

def logout_view(request):
    logout(request)
    response = redirect('login')
    return response