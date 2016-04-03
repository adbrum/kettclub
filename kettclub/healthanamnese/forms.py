from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from kettclub.healthanamnese.models import SaudeAnamnese

BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class HealthAnamneseForm(ModelForm):
    atleta = forms.IntegerField(label='Nº do atleta', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width:50px'}))

    # DOENÇA CONHECIDA CARDIOVASCULAR E/OU PULMONAR#
    quest01 = forms.ChoiceField(BOOL_CHOICES,
                                label=('Doença cardiovascular ou pulmonar (asma, bronquite, etc.)'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest02 = forms.ChoiceField(BOOL_CHOICES,
                                label=('Doença metabólica (tiroide, renal ou hepática'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest03 = forms.ChoiceField(BOOL_CHOICES,
                                label=('Diabetes tipo I ou II'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest04 = forms.ChoiceField(BOOL_CHOICES,
                                label=('Dor ou desconforto no peito em repouso ou exercício'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest05 = forms.ChoiceField(BOOL_CHOICES,
                                label=('Desmaios, tonturas ou perda de consciência'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest06 = forms.ChoiceField(BOOL_CHOICES,
                                label=(
                                    'Dificuldades em respirar ou problemas respiratórios repentinos durante a noite'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest07 = forms.ChoiceField(BOOL_CHOICES,
                                label=(
                                    'Palpitações ou taquicardia'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest08 = forms.ChoiceField(BOOL_CHOICES,
                                label=(
                                    'Dor severa nas pernas durante a marcha'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest09 = forms.ChoiceField(BOOL_CHOICES,
                                label=(
                                    'Tensão arterial maior que 140/90 mm Hg ou sob medicação'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest010 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Edema no tornozelo'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    # DOENÇA CORONÁRIA#
    quest011 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Colesterol Total maior que 240 mg/dl ou sob medicação'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    quest012 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'História familiar de enfarte do miocárdio ou morte súbita do pai/mãe ou outro familiar em primeiro grau antes dos 55/65 anos'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    quest013 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Índice de Massa Corporal maior que 30 (kg/m2)'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    quest014 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Fumador ou que tenha deixado de fumar nos últimos 6 mese'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest015 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Sem programa de exercício regular há mais de 6 meses'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    # OUTRAS SITUAÇÕES ASSOCIADAS AO SEU ESTADO DE SAÚDE#
    quest016 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Algum problema de saúde não mencionado e/ou qualquer outro fator condicionante do programa de exercício físico a elaborar?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest017 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Doença recente?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest018 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Hospitalização recente?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest019 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Procedimentos cirúrgicos?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    # ANAMINESE DESPORTIVA#
    quest020 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Pratica algum tipo de exercício regularmente fora do KC?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest021 = forms.CharField(required=False,
                               label=(
                                   'Se sim, qual e quantas vezes por semana?'),
                               widget=forms.Textarea(
                                   attrs={'class': 'form-control input-sm'}))

    quest022 = forms.CharField(required=False,
                               label=(
                                   'Alguma observação importante a declarar?'),
                               widget=forms.Textarea(
                                   attrs={'class': 'form-control input-sm'}))

    quest023 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Declara que compreendeu integralmente o conteúdo deste documento?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    class Meta:
        model = SaudeAnamnese
        fields = '__all__'


class EditHealthAnamneseForm(ModelForm):
    # DOENÇA CONHECIDA CARDIOVASCULAR E/OU PULMONAR#
    quest01 = forms.ChoiceField(BOOL_CHOICES,
                                label=('Doença cardiovascular ou pulmonar (asma, bronquite, etc.)'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest02 = forms.ChoiceField(BOOL_CHOICES,
                                label=('Doença metabólica (tiroide, renal ou hepática'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest03 = forms.ChoiceField(BOOL_CHOICES,
                                label=('Diabetes tipo I ou II'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest04 = forms.ChoiceField(BOOL_CHOICES,
                                label=('Dor ou desconforto no peito em repouso ou exercício'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest05 = forms.ChoiceField(BOOL_CHOICES,
                                label=('Desmaios, tonturas ou perda de consciência'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest06 = forms.ChoiceField(BOOL_CHOICES,
                                label=(
                                    'Dificuldades em respirar ou problemas respiratórios repentinos durante a noite'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest07 = forms.ChoiceField(BOOL_CHOICES,
                                label=(
                                    'Palpitações ou taquicardia'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest08 = forms.ChoiceField(BOOL_CHOICES,
                                label=(
                                    'Dor severa nas pernas durante a marcha'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest09 = forms.ChoiceField(BOOL_CHOICES,
                                label=(
                                    'Tensão arterial maior que 140/90 mm Hg ou sob medicação'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest010 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Edema no tornozelo'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    # DOENÇA CORONÁRIA#
    quest011 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Colesterol Total maior que 240 mg/dl ou sob medicação'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    quest012 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'História familiar de enfarte do miocárdio ou morte súbita do pai/mãe ou outro familiar em primeiro grau antes dos 55/65 anos'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    quest013 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Índice de Massa Corporal maior que 30 (kg/m2)'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    quest014 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Fumador ou que tenha deixado de fumar nos últimos 6 mese'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest015 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Sem programa de exercício regular há mais de 6 meses'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    # OUTRAS SITUAÇÕES ASSOCIADAS AO SEU ESTADO DE SAÚDE#
    quest016 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Algum problema de saúde não mencionado e/ou qualquer outro fator condicionante do programa de exercício físico a elaborar?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest017 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Doença recente?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest018 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Hospitalização recente?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest019 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Procedimentos cirúrgicos?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    # ANAMINESE DESPORTIVA#
    quest020 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Pratica algum tipo de exercício regularmente fora do KC?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest021 = forms.CharField(required=False,
                               label=(
                                   'Se sim, qual e quantas vezes por semana?'),
                               widget=forms.Textarea(
                                   attrs={'class': 'form-control input-sm'}))

    quest022 = forms.CharField(required=False,
                               label=(
                                   'Alguma observação importante a declarar?'),
                               widget=forms.Textarea(
                                   attrs={'class': 'form-control input-sm'}))

    quest023 = forms.ChoiceField(BOOL_CHOICES,
                                 label=(
                                     'Declara que compreendeu integralmente o conteúdo deste documento?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    class Meta:
        model = SaudeAnamnese
        exclude = ['atleta']
        fields = '__all__'

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
