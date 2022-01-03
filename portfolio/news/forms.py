from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'date']

        widgets = {

            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of publication'
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text'
            })

        }
