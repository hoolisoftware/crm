from . import widgets
from typing import Tuple, Dict
from django.utils.translation import gettext_lazy as _

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()


class UserSignUpForm(UserCreationForm):
    common_attributes = {
        'class': 'form-control'
    }

    def __init__(self, *args: Tuple, **kwargs: Dict) -> None:
        super().__init__(*args, **kwargs)
        self.add_widgets_to_fields()

    def add_widgets_to_fields(self) -> None:
        self.fields['email'].widget = forms.TextInput(attrs={
            **self.common_attributes,
        })

        self.fields['first_name'].widget = forms.TextInput(attrs={
            **self.common_attributes,
        })

        self.fields['last_name'].widget = forms.TextInput(attrs={
            **self.common_attributes,
        })

        self.fields['password1'].widget = forms.PasswordInput(attrs={
            **self.common_attributes,
            'addon': 'password-addon'
        })

        self.fields['password2'].widget = forms.PasswordInput(attrs={
            **self.common_attributes,
            'addon': 'confirm-password-addon'
        })

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

        labels = {
            'email': _('Email'),
            'password1': _('Password'),
            'password2': _('Confirm password')
        }


class UserSignInForm(AuthenticationForm):
    common_attributes = {
        'class': 'form-control'
    }

    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label=_('Remember me')
    )

    def __init__(self, *args: Tuple, **kwargs: Dict) -> None:
        super().__init__(*args, **kwargs)
        self.add_widgets_to_fields()

    def add_widgets_to_fields(self) -> None:
        self.fields['username'].label = _('Email')
        self.fields['username'].widget = forms.TextInput(attrs={
            **self.common_attributes,
        })

        self.fields['password'].label = _('Password')
        self.fields['password'].widget = widgets.PasswordWidget(attrs={
            **self.common_attributes,
            'addon': 'password-addon'
        })
