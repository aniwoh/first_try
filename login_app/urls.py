from django.urls import path
from login_app import views
from homepage import views as homeview
from django.views.generic import RedirectView

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('register',views.register,name='register'),
    path('', RedirectView.as_view(url='login')),
    path('homepage',homeview.homepage),
    path('logout',views.logout_view,name='logout')
]