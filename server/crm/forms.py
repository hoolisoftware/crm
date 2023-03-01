from django import forms

from core import mixins
from . import models


class PositionDutyForm(mixins.AddClassNameMixin, forms.ModelForm):

    class Meta:
        model = models.PositionDuty
        widgets = {
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }
        exclude = (
            'employee',
            'paid',
        )


class PositionDutyDateForm(mixins.AddClassNameMixin, forms.ModelForm):
    class Meta:
        model = models.PositionDuty
        widgets = {
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }
        exclude = (
            'employee',
            'date',
            'paid',
        )


class PositionDutyProjectForm(mixins.AddClassNameMixin, forms.ModelForm):

    class Meta:
        model = models.PositionDuty
        widgets = {
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }
        fields = '__all__'


class PositionDutyProjectDateForm(mixins.AddClassNameMixin, forms.ModelForm):

    class Meta:
        model = models.PositionDuty
        widgets = {
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }
        exclude = ('date',)

