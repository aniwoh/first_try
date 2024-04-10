from django.urls import path
from api import views
from django.views.generic import RedirectView

urlpatterns = [
    path('proxy_get_index_photo',views.proxy_get_index_photo,name='proxy_get_index_photo'),
    path('like_comment',views.api_like_comment,name='like_comment'),
    path('dislike_comment',views.api_dislike_comment,name='dislike_comment'),
    path('like_article',views.api_like_article,name='like_article'),
    path('dislike_article',views.api_dislike_article,name='dislike_article'),
    path('iframe/<str:filename>',views.api_get_iframe,name='iframe'),
    path('get_user_json',views.api_get_user_json,name='get_user_json'),
    path('delete_user',views.api_delete_user,name='delete_user'),
    path('get_alltags',views.api_get_alltags,name='get_alltags'),
    path('filter_articles',views.api_filter_articles,name='filter_articles'),
]