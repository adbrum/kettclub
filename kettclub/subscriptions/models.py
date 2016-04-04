from django.core.urlresolvers import reverse
from django.db import models
from kettclub.monthlyplans.models import PlanoMensalidade

BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))


class Subscription(models.Model):
    planomensalidade = models.ForeignKey(PlanoMensalidade, verbose_name='Planos e mensalidade')
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    emailatleta = models.EmailField('Email', max_length=50, blank=True)
    datainicio = models.DateField('Data de inicio')
    datanascimento = models.DateField('Data de nascimento')
    idade = models.IntegerField('Idade', blank=True)
    cc = models.CharField('Cartão do Cidadão', max_length=12)
    nif = models.IntegerField('Número de Identifacação Fiscal')
    telefone = models.CharField('Nº Telefone', max_length=9)
    telefone2 = models.CharField('Nº Telefone urgência', max_length=9, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=True, choices=BOOL_CHOICES)

    class Meta:
        verbose_name_plural = 'Inscrições Atletas'
        verbose_name = 'Inscrição Atleta'
        ordering = ('nome',)

    def get_absolute_url(self):
        return reverse('editatleta', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.pk)  # self.nome + ' ' + self.sobrenome