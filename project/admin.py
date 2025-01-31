# project/admin.py
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "customer_name", "start_date", "status", "budget", "cost"]
    search_fields = ["name", "customer_name"]
    list_filter = ["status", "start_date", "end_date"]
    ordering = ["-start_date"]
