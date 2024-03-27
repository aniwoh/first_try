"""
URL configuration for first_try project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    # path('', views.fix_web),
    path('admin/', admin.site.urls),
    path('',include('index_app.urls')),
    path('index/',include('index_app.urls')),
    path('user/',include('login_app.urls')),
    path('homepage/',include('homepage.urls')),
    path('layer/<str:page_name>.html',views.layer_view,name='layer'),
]

# 将自定义的视图与 400 错误关联
handler400 = views.bad_request400
handler403 = views.permission_denied403
handler404 = views.page_not_found404
handler429 = views.page_not_found429
handler500 = views.server_error500
handler502 = views.server_error502
handler503 = views.server_error503
handler504 = views.server_error504
