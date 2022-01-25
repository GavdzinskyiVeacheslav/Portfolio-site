from modeltranslation.translator import register, TranslationOptions
from notes.models import Articles

@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ('title', 'full_text')


