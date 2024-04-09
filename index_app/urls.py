from django.urls import path
from index_app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',views.index,name='index'),
    path('post',views.post,name='post'),
    path('category',views.category,name='category'),
    path('post_comment', views.post_comment, name='post_comment'),
    path('like_comment', views.like_comment, name='like_comment'),
    path('dislike_comment', views.dislike_comment, name='dislike_comment'),
    path('like_article', views.like_article, name='like_article'),
    path('dislike_article', views.dislike_article, name='dislike_article'),
    path('filter_articles', views.filter_articles, name='filter_articles'),
]