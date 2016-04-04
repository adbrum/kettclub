from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from kettclub.monthlyplans.models import PlanoMensalidade
from kettclub.subscriptions.models import Subscription

BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))


class SubscriptionForm(ModelForm):
    error_messages = {
        'err_code': (u"Já existe uma função com essa sigla."),
        'required': (u'O campo é obrigatório.'),
    }

    nome = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    sobrenome = forms.CharField(label='Sobrenome', widget=forms.TextInput(
        attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))
    emailatleta = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}))
    datainicio = forms.DateField(label='Data inicio',
                                 widget=forms.DateInput(
                                     attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control date mask-date',
                                            ' data-provide': 'datepicker',
                                            'data-date-format': 'dd/mm/yyyy'}))
    datanascimento = forms.DateField(label='Data de Nascimento',
                                     widget=forms.DateInput(
                                         attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control date',
                                                ' data-provide': 'datepicker',
                                                'data-date-format': 'dd/mm/yyyy'}))
    idade = forms.CharField(label='Idade', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Idade', 'class': 'form-control'}))
    nif = forms.CharField(label='NIF', widget=forms.TextInput(
        attrs={'placeholder': 'Número de identificação fiscal', 'class': 'form-control'}))
    cc = forms.CharField(label='CC', widget=forms.TextInput(
        attrs={'placeholder': 'Cartão do Cidadão', 'class': 'form-control'}))

    telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Contato', 'class': 'form-control'}))
    telefone2 = forms.CharField(label='Telefone 2', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Contato urgente', 'class': 'form-control'}))
    # planomensalidade = forms.CharField(label='Plano', widget=forms.TextInput(
    #     attrs={'placeholder': 'Plano mensalidade', 'class': 'form-control'}))

    planomensalidade = forms.ModelChoiceField(PlanoMensalidade.objects.all(),
                                              label=('Plano'),
                                              widget=forms.Select(attrs={'placeholder': 'Plano mensalidade',
                                                                         'class': 'form-control input-sm medio required_form'})
                                              )

    class Meta:
        model = Subscription
        # model = PlanoMensalidade
        fields = ['nome', 'sobrenome', 'emailatleta', 'datainicio', 'datanascimento', 'idade', 'nif', 'cc', 'telefone',
                  'telefone2', 'planomensalidade']

    def clean_code(self):
        emailatleta = self.cleaned_data["emailatleta"]
        if self.emailatleta != emailatleta:
            try:
                Subscription.objects.get(emailatleta=emailatleta)
            except Subscription.DoesNotExist:
                return emailatleta
            raise forms.ValidationError(self.error_messages['err_code'])
        else:
            return emailatleta


class EditSubscriptionForm(ModelForm):
    error_messages = {
        'err_code': (u"Já existe uma função com essa sigla."),
        'required': (u'O campo é obrigatório.'),
    }

    ativo = forms.ChoiceField(BOOL_CHOICES,
                              label=('Ativo'),
                              widget=forms.Select(attrs={'placeholder': '--',
                                                         'class': 'form-control input-sm medio required_form'})
                              )
    nome = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    sobrenome = forms.CharField(label='Sobrenome', widget=forms.TextInput(
        attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))
    emailatleta = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}))
    datainicio = forms.DateField(label='Data inicio',
                                 widget=forms.DateInput(
                                     attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control date',
                                            ' data-provide': 'datepicker',
                                            'data-date-format': 'dd/mm/yyyy'}))
    datanascimento = forms.DateField(label='Data de Nascimento',
                                     widget=forms.DateInput(
                                         attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control date',
                                                ' data-provide': 'datepicker',
                                                'data-date-format': 'dd/mm/yyyy'}))
    idade = forms.CharField(label='Idade', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Idade', 'class': 'form-control'}))
    nif = forms.CharField(label='NIF', widget=forms.TextInput(
        attrs={'placeholder': 'Número de identificação fiscal', 'class': 'form-control'}))
    cc = forms.CharField(label='CC', widget=forms.TextInput(
        attrs={'placeholder': 'Cartão do Cidadão', 'class': 'form-control'}))

    telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Contato', 'class': 'form-control'}))
    telefone2 = forms.CharField(label='Telefone 2', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Contato urgente', 'class': 'form-control'}))
    # planomensalidade = forms.CharField(label='Plano', widget=forms.TextInput(
    #     attrs={'placeholder': 'Plano mensalidade', 'class': 'form-control'}))

    planomensalidade = forms.ModelChoiceField(PlanoMensalidade.objects.all(),
                                              label=('Plano'),
                                              widget=forms.Select(attrs={'placeholder': 'Plano mensalidade',
                                                                         'class': 'form-control input-sm medio required_form'})
                                              )

    class Meta:
        model = Subscription
        # model = PlanoMensalidade
        fields = ['ativo', 'nome', 'sobrenome', 'emailatleta', 'datainicio', 'datanascimento', 'idade', 'nif', 'cc',
                  'telefone',
                  'telefone2', 'planomensalidade']

    # def __init__(self, emailatleta, *args, **kwargs):
    #     super(EditSubscriptionForm, self).__init__(*args, **kwargs)
    #     self.emailatleta = emailatleta

    def clean_code(self):
        emailatleta = self.cleaned_data["emailatleta"]
        if self.emailatleta != emailatleta:
            try:
                Subscription.objects.get(emailatleta=emailatleta)
            except Subscription.DoesNotExist:
                return emailatleta
            raise forms.ValidationError(self.error_messages['err_code'])
        else:
            return emailatleta


# class FichaSubscriptionForm(ModelForm):
#     nome = forms.CharField(label='Nome', widget=forms.TextInput(
#         attrs={'placeholder': 'Nome', 'class': 'form-control'}))
#     sobrenome = forms.CharField(label='Sobrenome', widget=forms.TextInput(
#         attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))
#     emailatleta = forms.EmailField(label='Email', widget=forms.TextInput(
#         attrs={'placeholder': 'Email', 'class': 'form-control'}))
#     datainicio = forms.DateField(label='Data inicio',
#                                  widget=forms.DateInput(
#                                      attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control date',
#                                             ' data-provide': 'datepicker',
#                                             'data-date-format': 'dd/mm/yyyy'}))
#     datanascimento = forms.DateField(label='Data de Nascimento',
#                                      widget=forms.DateInput(
#                                          attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control date',
#                                                 ' data-provide': 'datepicker',
#                                                 'data-date-format': 'dd/mm/yyyy'}))
#     idade = forms.CharField(label='Idade', required=False, widget=forms.TextInput(
#         attrs={'placeholder': 'Idade', 'class': 'form-control'}))
#     nif = forms.CharField(label='NIF', widget=forms.TextInput(
#         attrs={'placeholder': 'Número de identificação fiscal', 'class': 'form-control'}))
#     cc = forms.CharField(label='CC', widget=forms.TextInput(
#         attrs={'placeholder': 'Cartão do Cidadão', 'class': 'form-control'}))
#
#     telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(
#         attrs={'placeholder': 'Contato', 'class': 'form-control'}))
#     telefone2 = forms.CharField(label='Telefone 2', required=False, widget=forms.TextInput(
#         attrs={'placeholder': 'Contato urgente', 'class': 'form-control'}))
#     # planomensalidade = forms.CharField(label='Plano', widget=forms.TextInput(
#     #     attrs={'placeholder': 'Plano mensalidade', 'class': 'form-control'}))
#
#     planomensalidade = forms.ModelChoiceField(PlanoMensalidade.objects.all(),
#                                               label=('Plano'),
#                                               widget=forms.Select(attrs={'placeholder': 'Plano mensalidade',
#                                                                          'class': 'form-control input-sm medio required_form'})
#                                               )
#
#     def __init__(self, *args, **kwargs):
#         super(FichaSubscriptionForm, self).__init__(*args, **kwargs)
#         # self.fields['coordenacao'].widget.attrs['disabled'] = "disabled"
