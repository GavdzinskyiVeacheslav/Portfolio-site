from django.contrib import admin
from .models import Articles
from modeltranslation.admin import TranslationAdmin
from notes.models import *

@admin.register(Articles)
class ArticlesTranslationOptions(TranslationAdmin):
    fields = ('title', 'full_text')


