from modeltranslation.translator import register, TranslationOptions
from notes.models import *

@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ('title', 'full_text')


