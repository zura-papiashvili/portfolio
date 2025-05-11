# api/views.py
from django.http import JsonResponse
from django.utils.translation import get_language
from project.models import Service, Project
from blog.models import FAQ, Author  # Assuming Author model exists in blog.models


def services_list(request):
    language = get_language()
    services = Service.objects.exclude(**{f"title_{language}": ""})[:3]

    data = []
    for service in services:
        data.append(
            {
                "id": service.id,
                "title": getattr(service, f"title_{language}"),
                "description": getattr(service, f"description_{language}"),
                "price_range": service.price_range,
                "features": service.get_features(),  # this should return a list
                "ideal_for": service.get_ideal_for(),  # this too
            }
        )

    return JsonResponse(data, safe=False)


def faqs_main_list(request):
    language = get_language()
    faqs = FAQ.objects.filter(main=True).exclude(**{f"question_{language}": ""})[:3]

    data = []
    for faq in faqs:
        data.append(
            {
                "question": getattr(faq, f"question_{language}"),
                "answer": getattr(faq, f"answer_{language}"),
            }
        )

    return JsonResponse(data, safe=False)


def projects_list_api(request):
    projects = Project.objects.all().order_by("-start_date")

    data = [
        {
            "name": p.name,
            "customer_name": p.customer_name,
            "status": p.get_status_display(),
            "status_code": p.status,
            "start_date": p.start_date.strftime("%Y-%m-%d"),
            "end_date": p.end_date.strftime("%Y-%m-%d") if p.end_date else None,
            "budget": float(p.budget),
            "cost": float(p.cost) if p.cost else None,
            "description": p.description,
            "project_video": p.project_video,
            "image_url": p.image.url if p.image else None,
        }
        for p in projects
    ]
    return JsonResponse(data, safe=False)


def faqs_list_api(request):
    language = get_language()
    faqs = FAQ.objects.exclude(**{f"question_{language}": ""})

    data = [
        {
            "question": getattr(faq, f"question_{language}"),
            "answer": getattr(faq, f"answer_{language}"),
        }
        for faq in faqs
    ]

    return JsonResponse(data, safe=False)


def authors_list_api(request):

    authors = Author.objects.all()

    data = [
        {
            "id": author.id,
            "first_name": author.first_name,
            "last_name": author.last_name,
            "bio": author.bio,
            "image_url": author.image.url if author.image else None,
        }
        for author in authors
    ]

    return JsonResponse(data, safe=False)
