from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator

from .models import Blog

class BlogTranslationOptions(TranslationOptions):
    fields = ( 'title', 'description',)


translator.register(Blog, BlogTranslationOptions)