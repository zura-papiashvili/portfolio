from django.shortcuts import get_object_or_404, render
from .models import Author, Post, FAQ, Carousel, RestrictedPage, ZoomEvent
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


def home(request):
    language = get_language()  # or request.LANGUAGE_CODE
    events = ZoomEvent.objects.filter(access_type="public").all()
    faqs = FAQ.objects.exclude(**{f"question_{language}": ""}).all()
    authors = Author.objects.all()[:3]
    services = Service.objects.exclude(**{f"title_{language}": ""}).all()[:3]
    projects = Project.objects.exclude(**{f"name_{language}": ""}).all()[:3]

    return render(
        request,
        "blog/home.html",
        {
            "faqs": faqs,
            "authors": authors,
            "events": events,
            "projects": projects,
            "services": services,
        },
    )


def about(request):
    authors = Author.objects.all()
    return render(request, "about.html", {"authors": authors})


# def contact(request):
#     return render(request, "contact.html")


def posts(request):
    posts = Post.objects.filter(access_type="public").order_by("-date")
    return render(request, "blog/posts.html", {"posts": posts})


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


def restricted_page_view(request):
    page = get_object_or_404(RestrictedPage)  # There is only one page, so just fetch it
    form = AccessCodeForm(request.POST or None)

    # Check if the user has already entered the correct code
    if request.session.get("access_granted", False):
        posts = Post.objects.filter(access_type="private").order_by("-date")
        events = ZoomEvent.objects.filter(access_type="private").all()
        return render(
            request,
            "restricted_page.html",
            {"page": page, "posts": posts, "events": events},
        )

    if request.method == "POST" and form.is_valid():

        if form.cleaned_data["code"] == page.access_code:
            # Store that the user has entered the correct code
            request.session["access_granted"] = True
            posts = Post.objects.filter(access_type="private").order_by("-date")
            events = ZoomEvent.objects.filter(access_type="private").all()
            return render(
                request,
                "restricted_page.html",
                {"page": page, "posts": posts, "events": events},
            )
        else:
            # If the code doesn't match, deny access
            return render(request, "restricted_denied.html", {"page": page})

    # Render the form if the code hasn't been submitted yet
    return render(request, "enter_code.html", {"form": form, "page": page})


def zoom_events(request):
    events = ZoomEvent.objects.all()
    return render(request, "zoom_events.html", {"events": events})


def switch_language(request, language):
    activate(language)
    request.session[settings.LANGUAGE_COOKIE_NAME] = language
    response = redirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)  # Set language cookie
    return response
