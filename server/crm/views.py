from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'origin/base.django-html'


class RegisterView:
    pass


class LoginView:
    pass


class UserProjectListView:
    pass


class CreateProjectView:
    pass


class JoinProjectView:
    pass
