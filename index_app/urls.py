from django.urls import path
from index_app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',views.index,name='index'),
    path('post',views.post,name='post'),
]