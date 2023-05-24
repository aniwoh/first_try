from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # if username=='aniwoh' and password=='password':
        #     return redirect('/index')
        # else:
        #     error_message = "账号或密码错误"
        #     return render(request, 'login.html', {'error_message': error_message})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')  # 登录成功后重定向到主页
        else:
            error_message = "账号或密码错误"
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # 保存用户数据到数据库
            return redirect('login')  # 注册成功后重定向到登录页面
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})