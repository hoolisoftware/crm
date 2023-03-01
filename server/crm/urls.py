from django.urls import path

from . import views
from .urls_namespace import *  # noqa ignore=F405

app_name = 'crm'

urlpatterns = [
    path('',
         views.AccountCalendarView.as_view(),
         name=ACCOUNT_CALENDAR),  # noqa ignore=F405

    path('dashboard/', views.AccountDashboardView.as_view(), name=ACCOUNT_DASHBOARD),  # noqa ignore=F405

    # Employee

    path('api/account/duty/<int:y>/<int:m>/', views.account_duty),
    path('api/duty/<int:y>/<int:m>/', views.project_duty),

    path('account/duty/table/',
         views.AccountDutyTableView.as_view(),
         name=ACCOUNT_DUTY_TABLE), # noqa ignore=F405

    path('account/duty/create/',
         views.AccountDutyCreateView.as_view(),
         name=ACCOUNT_DUTY_CREATE), # noqa ignore=F405

    path('account/duty/create/<int:y>/<int:m>/<int:d>/',
         views.AccountDutyCreateDateView.as_view(),
         name=ACCOUNT_DUTY_CREATE_DATE), # noqa ignore=F405

    path('account/duty/<int:pk>/update/',
         views.AccountDutyUpdateView.as_view(),
         name=ACCOUNT_DUTY_UPDATE), # noqa ignore=F405

    path('account/duty/<int:pk>/',
         views.AccountDutyDetailView.as_view(),
         name=ACCOUNT_DUTY_DETAIL),  # noqa ignore=F405

    path('project/calendar', views.ProjectCalendarView.as_view(), name=PROJECT_CALENDAR), # noqa ignore=F405
    path('project/duty/table/', views.ProjectDutyTableView.as_view(), name=PROJECT_DUTY_TABLE), # noqa ignore=F405
    path('project/duty/table/<int:pk>/', views.ProjectDutyTableAccountView.as_view(), name=PROJECT_DUTY_TABLE_ACCOUNT), # noqa ignore=F405
    path('project/duty/create/', views.ProjectDutyCreateView.as_view(), name=PROJECT_DUTY_CREATE), # noqa ignore=F405
    path('project/duty/create/<int:y>/<int:m>/<int:d>/', views.ProjectDutyCreateDateView.as_view(), name=PROJECT_DUTY_CREATE_DATE), # noqa ignore=F405
    path('project/duty/<int:pk>/update', views.ProjectDutyUpdateView.as_view(), name=PROJECT_DUTY_UPDATE), # noqa ignore=F405
    path('project/duty/<int:pk>/', views.ProjectDutyDetailView.as_view(), name=PROJECT_DUTY_DETAIL), # noqa ignore=F405

]
