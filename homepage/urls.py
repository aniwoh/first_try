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
    path('getAllArticleByLevel/', views.getAllArticleByLevel, name='getAllArticleByLevel'),
    path('deleteArticleById', views.deleteArticleById, name='deleteArticleById'),
    path('edit', views.editArticleById, name='edit'),
]