from django.urls import path
from api import views
from django.views.generic import RedirectView

urlpatterns = [
    path('proxy_get_index_photo',views.proxy_get_index_photo,name='proxy_get_index_photo'),
]