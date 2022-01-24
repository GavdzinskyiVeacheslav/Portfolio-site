from  django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label=_(u'Логин'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label=_(u'Пароль'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label=_(u'Повтор пароля'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label=_(u'Логин'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label=_(u'Пароль'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))
