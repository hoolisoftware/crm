from django.urls import path

from . import views

app_name = 'users'


urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('password-forgot/',
         views.PasswordForgotView.as_view(), name='password-forgot')
]
