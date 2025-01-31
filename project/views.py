# project/views.py
from django.shortcuts import render
from .models import Project


def project_list(request):
    # Retrieve all projects from the database
    projects = Project.objects.all()

    # Pass the projects to the template
    return render(request, "project/project_list.html", {"projects": projects})
