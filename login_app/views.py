from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username=='aniwoh' and password=='password':
            return redirect('/index')
        else:
            error_message = "账号或密码错误"
            return render(request, 'login.html', {'error_message': error_message})

        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('index.html')  # 登录成功后重定向到主页
        # else:
        #     error_message = "Invalid username or password."
        #     return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')
