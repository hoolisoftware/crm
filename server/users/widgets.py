from django import forms


class PasswordWidget(forms.PasswordInput):
    template_name = 'users/widgets/password.django-html'
