from django.urls import path
from homepage import views
from django.views.generic import RedirectView

urlpatterns = [
    path('home',views.home,name='home'),
    path('list',views.list,name='list'),
    path('data',views.data,name='data'),
    path('userall',views.userall,name='userall'),
    path('setting',views.setting,name='setting'),
    path('', RedirectView.as_view(url='home')),
    path('upload/', views.upload_view, name='upload'),
    path('get_user_json/', views.get_user_json_api, name='get_user_json'),
    path('delete_user', views.delete_user, name='delete_user'),
]