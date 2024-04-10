from django.urls import path
from index_app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',views.index,name='index'),
    path('post',views.post,name='post'),
    path('category',views.category,name='category'),
    path('post_comment', views.post_comment, name='post_comment'),
    path('filter_articles', views.filter_articles, name='filter_articles'),
]