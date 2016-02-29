from django import forms
from django.forms import SelectDateWidget


class AssiduityForm(forms.Form):
    nome = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    sobrenome = forms.CharField(label='Sobrenome', widget=forms.TextInput(
        attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))
    date = forms.DateField(label='Data da presença')
