import profile
from re import template
from django.urls import path
from auth_system.views import *

# from django.contrib.auth.views import views as LoginView, LogoutView, PasswordResetView
from django.contrib.auth import views as authViews



urlpatterns = [
    path('profile/edit/', EditProfile, name='edit-profile'),
    path('signup/', Signup, name='signup'),
    path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(),
         {'next_page': 'index'}, name='logout'),
    path('change-password/', ChangePassword, name='change_password'),
    path('change-password/success', PasswordResetSuccess, name='passwordresetsuccess'),
    path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    path('passwordreset/success', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),




    

]
