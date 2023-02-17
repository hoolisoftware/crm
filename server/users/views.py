from django.views import generic


class SignUpView(generic.TemplateView):
    template_name = 'users/sign-up.django-html'


class SignInView(generic.TemplateView):
    template_name = 'users/sign-in.django-html'


class PasswordForgotView(generic.TemplateView):
    template_name = 'users/password-forgot.django-html'
