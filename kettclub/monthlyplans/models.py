from django.core.urlresolvers import reverse
from django.db import models

BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))


class PlanoMensalidade(models.Model):
    nome = models.CharField('Nome do plano', max_length=50)
    valor = models.DecimalField('Valor €', max_digits=5, decimal_places=2)
    horario = models.CharField('Horário', max_length=20)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=True, choices=BOOL_CHOICES)

    class Meta:
        verbose_name_plural = 'Planos e mensalidade'
        verbose_name = 'Plano e mensalidade'
        ordering = ('valor',)

    def get_absolute_url(self):
        return reverse('editatleta', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome + ' - ' + str(self.valor) + '€'
