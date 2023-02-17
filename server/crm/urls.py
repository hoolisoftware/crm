from django.urls import path

from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    # Employee
    path('account/positions/',
         views.AccountPositionDetailView.as_view(),
         name=''),

    path('account/positions/<int:pk>/',
         views.AccountPositionListView.as_view(),
         name=''),

    path('account/positions/<int:pk>/ok/',
         views.AccountPositionOkView.as_view(),
         name=''),

    path('account/positions/<int:pk>/ok-add/',
         views.AccountPositionOkAddView.as_view(),
         name=''),

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

    path('account/projects/positions/create/',
         views.AccountProjectPositionCreateView.as_view(),
         name='account-project-position-create'),

    path('account/projects/positions/<int:pk>/update/',
         views.AccountProjectPositionUpdateView.as_view(),
         name='account-project-position-update'),

    path('account/projects/positions/<int:pk>/add-employee/',
         views.AccountProjectPositionAddEmployeeView.as_view(),
         name='account-project-position-add-employee'),
]
