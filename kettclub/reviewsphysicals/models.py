from django.core.urlresolvers import reverse
from django.db import models
from kettclub.subscriptions.models import Atleta

BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))


class Avaliacao(models.Model):
    atleta = models.ForeignKey(Atleta, verbose_name='Nº do atleta')
    dataavaliacao = models.DateField('Data da avaliação')
    peso = models.DecimalField('Peso Kg', max_digits=4, decimal_places=2)
    metbasal = models.CharField('Met. basal Kcal', max_length=5)
    idadebiologica = models.IntegerField('Idade biológica anos')
    agua = models.DecimalField('Água %', max_digits=5, decimal_places=2)
    gorduraviceral = models.CharField('Gordura visceral nível', max_length=5)
    massaossea = models.DecimalField('Massa ossea kg', max_digits=4, decimal_places=2)
    massamuscular = models.DecimalField('Massa muscular total kg', max_digits=4, decimal_places=2)
    massagorda = models.DecimalField('Massa gorda total %', max_digits=4, decimal_places=2)
    pescoco = models.DecimalField('Pescoço cm', max_digits=4, decimal_places=2)
    ombros = models.DecimalField('Ombros cm', max_digits=4, decimal_places=2)
    peitos = models.DecimalField('Peitos cm', max_digits=4, decimal_places=2)
    cintura = models.DecimalField('Cintura cm', max_digits=4, decimal_places=2)
    abdominal = models.DecimalField('Abdominal cm', max_digits=4, decimal_places=2)
    quadril = models.DecimalField('Quadril cm', max_digits=4, decimal_places=2)
    coxaproximal = models.DecimalField('Coxa proximal cm', max_digits=4, decimal_places=2)
    coxamedial = models.DecimalField('Coxa medial cm', max_digits=4, decimal_places=2)
    created_at = models.DateTimeField('Avaliado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Avaliações'
        verbose_name = 'Avaliação'
        ordering = ('atleta__nome',)

    def get_absolute_url(self):
        return reverse('editatleta', kwargs={'pk': self.pk})

    def __str__(self):
        return self.atleta.nome + ' ' + self.atleta.sobrenome
