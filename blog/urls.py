from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap  # Import your sitemaps
from .views import switch_language, offline_page


sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("events/", views.zoom_events, name="events"),
    path("posts/", views.posts, name="posts"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path("restricted/", views.restricted_page_view, name="restricted"),
    path("switch-language/<str:language>/", switch_language, name="switch_language"),
    path("offline/", offline_page, name="offline"),
]
