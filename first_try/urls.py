from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    # path('', views.fix_web),
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('',include('index_app.urls')), 
    path('index/',include('index_app.urls')),
    path('user/',include('login_app.urls')),
    path('homepage/',include('homepage.urls')),
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
