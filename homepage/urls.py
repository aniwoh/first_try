from django.urls import path
from homepage import views
from django.views.generic import RedirectView

urlpatterns = [
    path('home',views.home,name='home'),
    path('list',views.list,name='list'),
    path('data',views.data,name='data'),
    path('plugin',views.plugin,name='plugin'),
    path('setting',views.setting,name='setting'),
    path('', RedirectView.as_view(url='home')),
    path('upload/', views.upload_view, name='upload'),
]