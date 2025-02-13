from django.contrib import admin
from django.forms import DateTimeInput
from django import forms

from modeltranslation.admin import TranslationAdmin

# Register your models here.

from .models import (
    Author,
    Tag,
    Post,
    Comment,
    FAQ,
    CarouselImage,
    Carousel,
    RestrictedPage,
    ZoomEvent,
)


@admin.register(Author)
class AuthorAdmin(TranslationAdmin):
    list_display = ("last_name", "first_name", "email_address")
    search_fields = ("last_name", "first_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author")
    list_filter = ("author", "date", "tags")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post", "text")
    search_fields = ("user_name", "text")


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ("question", "answer", "main")  # Display translated fields
    search_fields = ("question", "answer", "main")  # Enable search functionality


class CarouselImageInline(admin.TabularInline):
    model = CarouselImage
    extra = 1


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    inlines = [CarouselImageInline]
    list_display = ("title", "description")
    search_fields = ("title", "description")


@admin.register(RestrictedPage)
class RestrictedPageAdmin(admin.ModelAdmin):
    list_display = ("title", "access_code")
    search_fields = ("title", "content")


# Define a custom form for the ZoomEvent admin
class ZoomEventForm(forms.ModelForm):
    class Meta:
        model = ZoomEvent
        fields = "__all__"

    # Override the event_time field to use a 'datetime-local' input
    event_time = forms.DateTimeField(
        widget=DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=["%Y-%m-%dT%H:%M"],  # Format matching the datetime-local input
    )


@admin.register(ZoomEvent)
class ZoomEventAdmin(admin.ModelAdmin):
    form = ZoomEventForm
    list_display = ["title", "event_time", "type", "access_type"]
    search_fields = ["title", "description"]


admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
