from django.urls import path
from api import views

urlpatterns = [
    path('like_comment',views.likeComment,name='like_comment'),
    path('dislike_comment',views.dislikeComment,name='dislike_comment'),
    path('like_article',views.likeArticle,name='like_article'),
    path('dislike_article',views.dislikeArticle,name='dislike_article'),
    path('iframe/<str:filename>',views.api_get_iframe,name='iframe'),
    path('get_user_json',views.api_get_user_json,name='get_user_json'),
    path('delete_user',views.delete_user,name='delete_user'),
    path('getAllTags',views.getAllTags,name='getAllTags'),
    path('filterArticles',views.filterArticles,name='filterArticles'),
    path('getAllArticles',views.getAllArticles,name='apiGetAllArticles'),
    path('searchArticles',views.searchArticles,name='searchArticles'),
    path('getArticleById',views.getArticleById,name='getArticleById'),
]