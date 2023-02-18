from . import forms
from . import mixins as custom_mixins

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.forms import Form
from django.contrib.auth import login
from django.http.response import HttpResponse


class SignUpView(custom_mixins.AlreadySignedInMixin, generic.CreateView):
    form_class = forms.UserSignUpForm
    template_name = 'users/sign-up.django-html'
    success_url = reverse_lazy('crm:home')
    redirect_authenticated_user = 'crm:home'


class SignInView(LoginView):
    form_class = forms.UserSignInForm
    template_name = 'users/sign-in.django-html'
    success_url = reverse_lazy('crm:home')

    redirect_authenticated_user = 'crm:home'

    def form_valid(self, form: Form) -> HttpResponse:

        if not form.cleaned_data['remember_me']:
            self.request.session.set_expiry(0)

        login(self.request, form.get_user())
        return super().form_valid(form)


class PasswordForgotView(generic.TemplateView):
    template_name = 'users/password-forgot.django-html'
