from . import forms
from . import mixins as custom_mixins

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.forms import Form
from django.contrib.auth import login
from django.http.response import HttpResponse

from . import forms


User = get_user_model()


class AccountView(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = 'users/account.django-html'
    form_class = forms.AccountUpdateForm
    success_url = reverse_lazy('users:account')
    success_message = 'Вы успешно обновили свои данные'

    def get_object(self):
        return self.request.user


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
