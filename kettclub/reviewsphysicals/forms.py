from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from kettclub.reviewsphysicals.models import Avaliacao
from kettclub.subscriptions.models import Subscription


class EvaluationForm(ModelForm):
    atleta = forms.ModelChoiceField(Subscription.objects.all().order_by('pk'),
                                    label=('Nome'),
                                    widget=forms.Select(attrs={'placeholder': 'Nome do atleta',
                                                               'class': 'form-control input-sm medio required_form'})
                                    )
    dataavaliacao = forms.DateField(label='Data avaliação',
                                    widget=forms.DateInput(
                                        attrs={'placeholder': 'dia/mês/ano', 'class': 'form-control date',
                                               ' data-provide': 'datepicker',
                                               'data-date-format': 'dd/mm/yyyy'}))

    peso = forms.DecimalField(label='Peso Kg', widget=forms.TextInput(
        attrs={'placeholder': 'Kg', 'class': 'form-control'}))

    metbasal = forms.DecimalField(label='Met. basal Kcal', widget=forms.TextInput(
        attrs={'placeholder': 'Kcal', 'class': 'form-control'}))

    idadebiologica = forms.IntegerField(label='Idade biológica anos', widget=forms.TextInput(
        attrs={'placeholder': 'Anos', 'class': 'form-control'}))

    agua = forms.DecimalField(label='Água %', widget=forms.TextInput(
        attrs={'placeholder': '%', 'class': 'form-control'}))

    gorduraviceral = forms.CharField(label='Gordura visceral nível', widget=forms.TextInput(
        attrs={'placeholder': 'Nível', 'class': 'form-control'}))

    massaossea = forms.DecimalField(label='Massa ossea kg', widget=forms.TextInput(
        attrs={'placeholder': 'Kg', 'class': 'form-control'}))

    massamuscular = forms.DecimalField(label='Massa muscular total kg', widget=forms.TextInput(
        attrs={'placeholder': 'Kg', 'class': 'form-control'}))

    massagorda = forms.DecimalField(label='Massa gorda total %', widget=forms.TextInput(
        attrs={'placeholder': '%', 'class': 'form-control'}))

    pescoco = forms.DecimalField(label='Pescoço cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    ombros = forms.DecimalField(label='Ombros cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    peitos = forms.DecimalField(label='Peitos cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    cintura = forms.DecimalField(label='Cintura cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    abdominal = forms.DecimalField(label='Abdominal cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    quadril = forms.DecimalField(label='Quadril cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    coxaproximal = forms.DecimalField(label='Coxa proximal cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    coxamedial = forms.DecimalField(label='Coxa medial cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    class Meta:
        model = Avaliacao
        exclude = ['created_at']


class EditEvaluationForm(ModelForm):
    dataavaliacao = forms.DateField(label='Data avaliação',
                                    widget=forms.DateInput(
                                        attrs={'placeholder': 'dia/mês/ano', 'class': 'form-control date',
                                               ' data-provide': 'datepicker',
                                               'data-date-format': 'dd/mm/yyyy'}))

    peso = forms.DecimalField(label='Peso Kg', widget=forms.TextInput(
        attrs={'placeholder': 'Kg', 'class': 'form-control'}))

    metbasal = forms.DecimalField(label='Met. basal Kcal', widget=forms.TextInput(
        attrs={'placeholder': 'Kcal', 'class': 'form-control'}))

    idadebiologica = forms.IntegerField(label='Idade biológica anos', widget=forms.TextInput(
        attrs={'placeholder': 'Anos', 'class': 'form-control'}))

    agua = forms.DecimalField(label='Água %', widget=forms.TextInput(
        attrs={'placeholder': '%', 'class': 'form-control'}))

    gorduraviceral = forms.CharField(label='Gordura visceral nível', widget=forms.TextInput(
        attrs={'placeholder': 'Nível', 'class': 'form-control'}))

    massaossea = forms.DecimalField(label='Massa ossea kg', widget=forms.TextInput(
        attrs={'placeholder': 'Kg', 'class': 'form-control'}))

    massamuscular = forms.DecimalField(label='Massa muscular total kg', widget=forms.TextInput(
        attrs={'placeholder': 'Kg', 'class': 'form-control'}))

    massagorda = forms.DecimalField(label='Massa gorda total %', widget=forms.TextInput(
        attrs={'placeholder': '%', 'class': 'form-control'}))

    pescoco = forms.DecimalField(label='Pescoço cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    ombros = forms.DecimalField(label='Ombros cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    peitos = forms.DecimalField(label='Peitos cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    cintura = forms.DecimalField(label='Cintura cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    abdominal = forms.DecimalField(label='Abdominal cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    quadril = forms.DecimalField(label='Quadril cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    coxaproximal = forms.DecimalField(label='Coxa proximal cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    coxamedial = forms.DecimalField(label='Coxa medial cm', widget=forms.TextInput(
        attrs={'placeholder': 'cm', 'class': 'form-control'}))

    class Meta:
        model = Avaliacao
        exclude = ['atleta', 'created_at']
