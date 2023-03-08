from django import forms

from core import mixins
from . import models


class PositionDutyFormMixin(mixins.AddClassNameMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['project'].queryset = models.Project.objects.filter(employees__exact=user) # noqa ignore


class PositionDutyForm(PositionDutyFormMixin):

    class Meta:
        model = models.PositionDuty
        widgets = {
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }
        exclude = (
            'employee',
            'paid',
        )


class PositionDutyDateForm(PositionDutyFormMixin):
    class Meta:
        model = models.PositionDuty
        widgets = {
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
        }
        exclude = (
            'employee',
            'date',
            'paid',
        )


class PositionDutyProjectForm(PositionDutyFormMixin):

    class Meta:
        model = models.PositionDuty
        widgets = {
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }
        fields = '__all__'


class PositionDutyProjectDateForm(PositionDutyFormMixin):

    class Meta:
        model = models.PositionDuty
        widgets = {
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
        }
        exclude = ('date',)

