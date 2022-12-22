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
    # path('test/', views.test, name='test'),
    path('home/', views.home, name='home'),
    path('pinned_job/', views.pinned_job, name='pinned_job'),
    path('delete_pinned_job/', views.delete_pinned_job, name='pinned_job'),
    path('post_job/', views.post_job, name='post_job'),
    path('posted_job/', views.posted_job, name='posted_job'),
    
    path('generate_view/', views.generate_view, name='generate_view'),
    path('delete_post_job/', views.delete_post_job, name='delete_post_job'),
]
