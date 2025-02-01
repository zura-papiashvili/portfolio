from modeltranslation.translator import translator, TranslationOptions
from .models import Project


class ProjectTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(Project, ProjectTranslationOptions)
