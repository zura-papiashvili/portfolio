from django.urls import path
from . import views

urlpatterns = [
    path("services/", views.services_list, name="api_services_list"),
    path("faqs-main/", views.faqs_main_list, name="faqs_main_list"),
    path("projects/", views.projects_list_api, name="projects_list_api"),
    path("faqs/", views.faqs_list_api, name="faqs_list_api"),
    path("authors/", views.authors_list_api, name="authors_list_api"),
]
