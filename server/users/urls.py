from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'users'


urlpatterns = [
    path('account/', views.AccountView.as_view(), name='account'),
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('password-forgot/',
         views.PasswordForgotView.as_view(), name='password-forgot'),
    path('logout/', LogoutView.as_view(), name='logout')
]
