# project/admin.py
from django.contrib import admin
from .models import Project, Service
from modeltranslation.admin import TranslationAdmin


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ["name", "customer_name", "start_date", "status", "budget", "cost"]
    search_fields = ["name", "customer_name"]
    list_filter = ["status", "start_date", "end_date"]
    ordering = ["-start_date"]


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ("title", "price_range", "created_at")
    search_fields = ("title",)
