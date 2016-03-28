from django import forms
from django.forms import SelectDateWidget, ModelForm
from kettclub.core.models import Presenca


class AssiduityForm(ModelForm):
    # nome = forms.CharField(label='Nome', widget=forms.TextInput(
    #     attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    # sobrenome = forms.CharField(label='Sobrenome', widget=forms.TextInput(
    #     attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))

    numeroatleta = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-text', 'name': 'numeromatricula', 'id': 'theDate', 'type': 'text'}))
    datapresenca = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-text', 'name': 'datapresenca', 'id': 'theDate', 'type': 'date'}))

    class Meta:
        model = Presenca
        fields = ['numeroatleta', 'datapresenca']
