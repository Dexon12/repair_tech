from django.urls import path, include
from .forms import ServiceAutocomplete

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home_view'),
    path('registration/', views.register, name='register_view'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('profile/', views.profile_view, name='profile_view'),
    path('service/<slug:service_slug>/', views.service_detail, name='service_detail'),
    path('contacts/', views.contacts_view, name='contacts_view'),
    path('service-autocomplete/', ServiceAutocomplete.as_view(), name='service-autocomplete'),
    path('search/', views.search_results, name='search_results'),

]
