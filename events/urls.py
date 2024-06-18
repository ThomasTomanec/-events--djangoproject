from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    # URLs for events
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('events/', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new/', views.event_new, name='event_new'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/delete/', views.event_delete_select, name='event_delete_select'),
    path('event/delete/<int:pk>/', views.event_delete_confirm, name='event_delete_confirm'),

    # URLs for clients
    path('clients/', views.client_list, name='client_list'),
    path('client/<int:pk>/', views.client_detail, name='client_detail'),
    path('client/new/', views.client_new, name='client_new'),
    path('client/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('client/delete/', views.client_delete_select, name='client_delete_select'),
    path('client/delete/<int:pk>/', views.client_delete_confirm, name='client_delete_confirm'),
]