from django.db import models
from kettclub.subscriptions.models import Atleta

BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))


class SaudeAnamnese(models.Model):
    atleta = models.OneToOneField(Atleta, verbose_name='Nº do atleta')
    # DOENÇA CONHECIDA CARDIOVASCULAR E/OU PULMONAR#
    quest01 = models.BooleanField('Doença cardiovascular ou pulmonar (asma, bronquite, etc.)', choices=BOOL_CHOICES)
    quest02 = models.BooleanField('Doença metabólica (tiroide, renal ou hepática)', choices=BOOL_CHOICES)
    quest03 = models.BooleanField('Diabetes tipo I ou II', choices=BOOL_CHOICES)
    quest04 = models.BooleanField('Dor ou desconforto no peito em repouso ou exercício', choices=BOOL_CHOICES)
    quest05 = models.BooleanField('Desmaios, tonturas ou perda de consciência', choices=BOOL_CHOICES)
    quest06 = models.BooleanField('Dificuldades em respirar ou problemas respiratórios repentinos durante a noite',
                                  choices=BOOL_CHOICES)
    quest07 = models.BooleanField('Palpitações ou taquicardia', choices=BOOL_CHOICES)
    quest08 = models.BooleanField('Dor severa nas pernas durante a marcha', choices=BOOL_CHOICES)
    quest09 = models.BooleanField('Tensão arterial maior que 140/90 mm Hg ou sob medicação', choices=BOOL_CHOICES)
    quest010 = models.BooleanField('Edema no tornozelo', choices=BOOL_CHOICES)
    # DOENÇA CORONÁRIA#
    quest011 = models.BooleanField('Colesterol Total maior que 240 mg/dl ou sob medicação', choices=BOOL_CHOICES)
    quest012 = models.BooleanField(
        'História familiar de enfarte do miocárdio ou morte súbita do pai/mãe ou outro familiar em primeiro grau antes dos 55/65 anos',
        choices=BOOL_CHOICES)
    quest013 = models.BooleanField('Índice de Massa Corporal maior que 30 (kg/m2)', choices=BOOL_CHOICES)
    quest014 = models.BooleanField('Fumador ou que tenha deixado de fumar nos últimos 6 meses', choices=BOOL_CHOICES)
    quest015 = models.BooleanField('Sem programa de exercício regular há mais de 6 meses', choices=BOOL_CHOICES)
    # OUTRAS SITUAÇÕES ASSOCIADAS AO SEU ESTADO DE SAÚDE#
    quest016 = models.BooleanField(
        'Algum problema de saúde não mencionado e/ou qualquer outro fator condicionante do programa de exercício físico a elaborar?',
        choices=BOOL_CHOICES)
    quest017 = models.BooleanField('Doença recente?', choices=BOOL_CHOICES)
    quest018 = models.BooleanField('Hospitalização?', choices=BOOL_CHOICES)
    quest019 = models.BooleanField('Procedimentos cirúrgicos?', choices=BOOL_CHOICES)
    # ANAMINESE DESPORTIVA#
    quest020 = models.BooleanField('Pratica algum tipo de exercício regularmente fora do KC?', choices=BOOL_CHOICES)
    quest021 = models.TextField('Se sim, qual e quantas vezes por semana?', blank=True)
    quest022 = models.TextField('Alguma observação importante a declarar?', blank=True)
    quest023 = models.BooleanField('Declara que compreendeu integralmente o conteúdo deste documento?',
                                   choices=BOOL_CHOICES)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Questionário de Saúde e Anamnese Desportiva'
        verbose_name = 'Questionário de Saúde e Anamnese Desportiva'
        # ordering = ('atleta__pk',)

    def __str__(self):
        return self.atleta.nome + ' ' + self.atleta.sobrenome
