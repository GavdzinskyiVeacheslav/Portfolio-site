from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text']

        widgets = {

            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Header'
            }),


            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text'
            })

        }
