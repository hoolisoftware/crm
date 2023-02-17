from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/home.django-html'


class AccountPositionDetailView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-position-detail.django-html'


class AccountPositionListView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-position-list.django-html'


class AccountPositionOkAddView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-position-ok.django-html'


class AccountPositionOkView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-position-ok-add.django-html'


class AccountProjectCreateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-project-create-update.django-html'


class AccountProjectUpdateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-project-create-update.django-html'


class AccountProjectDetailView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-project-detail.django-html'


class AccountProjectListView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-project-list.django-html'


class AccountProjectPositionAddEmployeeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-project-position-add-employee.django-html'


class AccountProjectPositionCreateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-project-position-create-update.django-html'


class AccountProjectPositionUpdateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-project-position-create-update.django-html'


class AccountProjectPositionDetailView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'crm/account-project-position-detail.django-html'
