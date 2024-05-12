from django.urls import path
from api import views
from django.views.generic import RedirectView

urlpatterns = [
    path('proxy_get_index_photo',views.proxyGetCardImage,name='proxy_get_index_photo'),
    path('like_comment',views.likeComment,name='like_comment'),
    path('dislike_comment',views.dislikeComment,name='dislike_comment'),
    path('like_article',views.likeArticle,name='like_article'),
    path('dislike_article',views.dislikeArticle,name='dislike_article'),
    path('iframe/<str:filename>',views.api_get_iframe,name='iframe'),
    path('get_user_json',views.api_get_user_json,name='get_user_json'),
    path('delete_user',views.delete_user,name='delete_user'),
    path('get_alltags',views.getAllTags,name='get_alltags'),
    path('filter_articles',views.filterArticles,name='filter_articles'),
    path('apiGetAllArticles',views.getAllArticles,name='apiGetAllArticles'),
    path('search_articles',views.searchArticles,name='search_articles'),
]