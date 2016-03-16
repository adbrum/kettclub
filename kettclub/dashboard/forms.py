from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Utilizador', widget=forms.TextInput(
        attrs={'placeholder': 'Nome ou email', 'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={'placeholder': 'Senha', 'class': 'form-control'}))

