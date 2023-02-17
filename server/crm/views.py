from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'crm/home.django-html'


class AccountPositionDetailView(generic.TemplateView):
    template_name = 'crm/account-position-detail.django-html'


class AccountPositionListView(generic.TemplateView):
    template_name = 'crm/account-position-list.django-html'


class AccountPositionOkAddView(generic.TemplateView):
    template_name = 'crm/account-position-ok.django-html'


class AccountPositionOkView(generic.TemplateView):
    template_name = 'crm/account-position-ok-add.django-html'


class AccountProjectCreateView(generic.TemplateView):
    template_name = 'crm/account-project-create-update.django-html'


class AccountProjectUpdateView(generic.TemplateView):
    template_name = 'crm/account-project-create-update.django-html'


class AccountProjectDetailView(generic.TemplateView):
    template_name = 'crm/account-project-detail.django-html'


class AccountProjectListView(generic.TemplateView):
    template_name = 'crm/account-project-list.django-html'


class AccountProjectPositionAddEmployeeView(generic.TemplateView):
    template_name = 'crm/account-project-position-add-employee.django-html'


class AccountProjectPositionCreateView(generic.TemplateView):
    template_name = 'crm/account-project-position-create-update.django-html'


class AccountProjectPositionUpdateView(generic.TemplateView):
    template_name = 'crm/account-project-position-create-update.django-html'


class AccountProjectPositionDetailView(generic.TemplateView):
    template_name = 'crm/account-project-position-detail.django-html'
