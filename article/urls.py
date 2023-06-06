from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView,PasswordChangeView


urlpatterns = [
    path('', Article_list),
    path('getarticle/',get_all_article,name='articlelist'),
    path('register', register,name='register'),
    path("article/<slug:slug>", article_details,name='article_details'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('password-change',PasswordChangeView.as_view(),name='password-change'),
    path('password-change-done',PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('add/',article_form,name='article_form'),
    path('update/<slug:slug>/', update_article, name='update_article'),
    path('delete/<slug:slug>/', delete_article, name='delete_article'),
    ]   
