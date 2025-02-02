from .models import Project, Service
from modeltranslation.translator import register, TranslationOptions


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("title", "description", "features", "ideal_for", "price_range")
