from django.shortcuts import get_object_or_404, render
from .models import Author, Post, FAQ, Carousel, RestrictedPage, ZoomEvent, WebProduct
from project.models import Project
from project.models import Service
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden
from .forms import AccessCodeForm
from portfolio.settings import EMAIL_HOST_USER
from django.shortcuts import redirect
from django.utils.translation import activate
from django.utils.translation import get_language
from django.http import JsonResponse


def home(request):

    return render(
        request,
        "blog/home.html",
    )


def about(request):
    return render(
        request,
        "about.html",
    )


def contact(request):
    if request.method == "POST":
        message_name = request.POST["message-name"]
        message_email = request.POST["message-email"]
        message = request.POST["message"]

        # Create a nicely formatted HTML message
        email_message = render_to_string(
            "email/contact_email.html",  # Create a new template for email content
            {
                "message_name": message_name,
                "message_email": message_email,
                "message": message,
            },
        )

        send_mail(
            f"Message from {message_name}",  # Subject
            "",  # No plain text message
            message_email,  # From email
            [settings.EMAIL_HOST_USER],  # To email
            html_message=email_message,  # HTML message content
        )

        return render(request, "contact.html", {"message_name": message_name})

    return render(request, "contact.html", {})


def web_products(request):
    return render(request, "web_products.html")


def switch_language(request, language):
    activate(language)
    request.session[settings.LANGUAGE_COOKIE_NAME] = language
    response = redirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)  # Set language cookie
    return response


def offline_page(request):
    return render(request, "offline.html")
