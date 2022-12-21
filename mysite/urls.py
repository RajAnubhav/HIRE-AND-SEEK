"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', views.company, name='company'),
    path('', views.index),
    path('login_company/', views.login_company, name='login_company'),
    path('login/', views.login, name='login'),
    path('settings/', views.settings, name='settings'),
    path('signup_company/', views.signup_company, name='signup_company'),
    path('signup/', views.signup, name='signup'),
    path('user/', views.user, name='user'),
    path('logout/', views.logout, name='logout'),
    path('test/', views.test, name='test'),
    path('home/', views.home, name='home'),
    path('pinned_job/', views.pinned_job, name='pinned_job'),
    path('delete_pinned_job/', views.delete_pinned_job, name='pinned_job'),
    path('post_job/', views.post_job, name='post_job'),
    path('posted_job/', views.posted_job, name='posted_job'),
    
    path('generate_view/', views.generate_view, name='generate_view'),
    path('delete_post_job/', views.delete_post_job, name='delete_post_job'),
]
