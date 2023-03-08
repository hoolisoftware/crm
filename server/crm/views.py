from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.http import JsonResponse

from . import models
from . import forms


User = get_user_model()


class AccountPositionDutyCreateUpdateViewMixin:
    def get_form(self):
        form = super().get_form()
        form.fields['project'].queryset = models.Project.objects.filter(employees__exact=self.request.user) # noqa ignore
        return form


class ProjectPositionDutyCreateUpdateViewMixin:
    def get_form(self):
        form = super().get_form()
        form.fields['project'].queryset = models.Project.objects.filter(owner__exact=self.request.user) # noqa ignore
        return form


class AccountDashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-dashboard.django-html'


class AccountCalendarView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/duty-calendar-account.django-html'


def account_duty(request, y, m):
    queryset = models.PositionDuty.objects.filter(
        employee=request.user,
        date__year=y,
        date__month=m
    )
    return JsonResponse({'duty': [
        {
            'id': object.id,
            'position': object.position,
            'date': object.date,
            'paid': object.paid,
        } for object in queryset
    ]})


def project_duty(request, y, m):
    queryset = models.PositionDuty.objects.filter(
        date__year=y,
        date__month=m
    )
    return JsonResponse({'duty': [
        {
            'id': object.id,
            'position': object.position,
            'date': object.date,
            'paid': object.paid,
        } for object in queryset
    ]})


# (Employee) Duty

class AccountDutyTableView(LoginRequiredMixin, generic.ListView):
    model = models.PositionDuty
    template_name = 'crm/duty-table-account.django-html'

    def get_queryset(self):
        return models.PositionDuty.objects.filter(employee=self.request.user)


class AccountDutyCreateView(
    AccountPositionDutyCreateUpdateViewMixin,
    SuccessMessageMixin,
    LoginRequiredMixin,
    generic.CreateView
):
    form_class = forms.PositionDutyForm
    template_name = 'crm/duty-create-update.django-html'
    success_message = 'Смена успешно создана!'

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class AccountDutyCreateDateView(
    AccountPositionDutyCreateUpdateViewMixin,
    SuccessMessageMixin,
    LoginRequiredMixin,
    generic.CreateView
):
    form_class = forms.PositionDutyDateForm
    template_name = 'crm/duty-create-update.django-html'
    success_message = 'Смена успешно создана!'

    def form_valid(self, form):
        form.instance.employee = self.request.user
        form.instance.date = date(self.kwargs['y'], self.kwargs['m'], self.kwargs['d']) # noqa ignore
        return super().form_valid(form)


class AccountDutyUpdateView(
    AccountPositionDutyCreateUpdateViewMixin,
    SuccessMessageMixin,
    LoginRequiredMixin,
    generic.UpdateView
):
    model = models.PositionDuty
    form_class = forms.PositionDutyForm
    template_name = 'crm/duty-create-update.django-html'
    success_message = 'Смена успешно изменена!'


class AccountDutyDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.PositionDuty
    template_name = 'crm/duty-detail.django-html'


# Duty (Project)


class ProjectCalendarView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/duty-calendar-project.django-html'


class ProjectDutyTableView(LoginRequiredMixin, generic.ListView):
    model = models.PositionDuty
    template_name = 'crm/duty-table-project.django-html'


class ProjectDutyTableAccountView(LoginRequiredMixin, generic.ListView):
    model = models.PositionDuty
    template_name = 'crm/duty-table.django-html'

    def get_queryset(self):
        return self.model.objects.filter(employee=User.objects.filter(id=self.kwargs['pk']).first())


class ProjectDutyCreateView(
    ProjectPositionDutyCreateUpdateViewMixin,
    LoginRequiredMixin,
    generic.CreateView
):
    model = models.PositionDuty
    form_class = forms.PositionDutyProjectForm
    template_name = 'crm/duty-create-update.django-html'


class ProjectDutyCreateDateView(
    ProjectPositionDutyCreateUpdateViewMixin,
    LoginRequiredMixin,
    generic.CreateView
):
    model = models.PositionDuty
    form_class = forms.PositionDutyProjectDateForm
    template_name = 'crm/duty-create-update.django-html'

    def form_valid(self, form):
        return super().form_valid(form)


class ProjectDutyUpdateView(
    ProjectPositionDutyCreateUpdateViewMixin,
    LoginRequiredMixin,
    generic.UpdateView
):
    model = models.PositionDuty
    form_class = forms.PositionDutyProjectForm
    template_name = 'crm/duty-create-update.django-html'


class ProjectDutyDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.PositionDuty
    template_name = 'crm/duty-detail.django-html'
