from django.contrib import admin
from django.forms import DateTimeInput
from django import forms

from modeltranslation.admin import TranslationAdmin

# Register your models here.

from .models import (
    Author,
    FAQ,
)


@admin.register(Author)
class AuthorAdmin(TranslationAdmin):
    list_display = ("last_name", "first_name", "email_address")
    search_fields = ("last_name", "first_name")

    list_filter = ("last_name", "first_name")


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ("question", "answer", "main")  # Display translated fields
    search_fields = ("question", "answer", "main")  # Enable search functionality
