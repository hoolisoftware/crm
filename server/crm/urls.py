from django.urls import path

from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    # Employee
    path('account/positions/',
         views.AccountPositionListView.as_view(),
         name='account-position-list'),

    path('account/positions/<int:pk>/',
         views.AccountPositionDetailView.as_view(),
         name='account-position-detail'),

    path('account/positions/<int:pk>/ok/',
         views.AccountPositionOkView.as_view(),
         name='account-position-ok'),

    path('account/positions/<int:pk>/ok-add/',
         views.AccountPositionOkAddView.as_view(),
         name='account-position-okadd'),

    # Employer
    path('account/projects/',
         views.AccountProjectListView.as_view(),
         name='account-project-list'),

    path('account/projects/<int:pk>/',
         views.AccountProjectDetailView.as_view(),
         name='account-project-detail'),

    path('account/projects/create/',
         views.AccountProjectCreateView.as_view(),
         name='account-project-create'),

    path('account/projects/<int:pk>/update',
         views.AccountProjectUpdateView.as_view(),
         name='account-project-update'),

    path('account/projects/positions/<int:pk>/',
         views.AccountProjectPositionDetailView.as_view(),
         name='account-project-position-detail'),

    path('account/projects/<int:pk>/positions/create/',
         views.AccountProjectPositionCreateView.as_view(),
         name='account-project-position-create'),

    path('account/projects/positions/<int:pk>/update/',
         views.AccountProjectPositionUpdateView.as_view(),
         name='account-project-position-update'),

    path('account/projects/positions/<int:pk>/add-employee/',
         views.AccountProjectPositionAddEmployeeView.as_view(),
         name='account-project-position-add-employee'),
]
