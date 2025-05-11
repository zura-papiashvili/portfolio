# project/views.py
from django.shortcuts import render
from .models import Project
from .models import Service
from django.http import JsonResponse
from django.utils.translation import get_language


def project_list(request):
    # Retrieve all projects from the database
    projects = Project.objects.all()

    # Pass the projects to the template
    return render(request, "project/project_list.html", {"projects": projects})


def services_api(request):
    language = get_language()  # or request.LANGUAGE_CODE
    services = Service.objects.exclude(**{f"title_{language}": ""}).all()
    return JsonResponse(
        {
            "services": [
                {
                    "id": service.id,
                    "title": getattr(service, f"title_{language}"),
                    "description": getattr(service, f"description_{language}"),
                    "features": getattr(service, f"get_features_{language}")(),
                    "ideal_for": getattr(service, f"get_ideal_for_{language}")(),
                    "price_range": getattr(service, f"price_range_{language}"),
                    "created_at": service.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                }
                for service in services
            ]
        },
        safe=False,
    )
