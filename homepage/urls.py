from django.urls import path
from homepage import views
from django.views.generic import RedirectView

urlpatterns = [
    path('home',views.home,name='home'),
    path('', RedirectView.as_view(url='home')),
]