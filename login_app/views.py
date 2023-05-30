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
        username = request.POST['username']
        password = request.POST['password1']
        confire_password=request.POST['password2']
        if password==confire_password:
            user = User.objects.create_user(
				username=username,
				password=password,
			)
            return redirect('login')  # 注册成功后重定向到登录页面
        else:
            error_message = "两次密码不一致"
            return render(request, 'register.html', {'error_message': error_message})
    
    return render(request, 'register.html')