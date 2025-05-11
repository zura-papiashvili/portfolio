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
    path("products/", views.web_products, name="products"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path("switch-language/<str:language>/", switch_language, name="switch_language"),
    path("offline/", offline_page, name="offline"),
]
