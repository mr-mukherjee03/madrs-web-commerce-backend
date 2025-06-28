from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views



urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ##path('login/', views.user_login, name='login'),
    #path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('register/', views.register, name='register'),
    path('',include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    
]
