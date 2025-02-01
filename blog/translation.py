from modeltranslation.translator import translator, TranslationOptions
from .models import FAQ, Author
from modeltranslation.translator import register, TranslationOptions


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ("question", "answer")


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ("first_name", "last_name", "bio")
