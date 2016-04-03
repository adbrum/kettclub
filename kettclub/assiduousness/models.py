from django.db import models
from kettclub.subscriptions.models import Atleta


class Presenca(models.Model):
    nome = models.CharField('Nome', max_length=50)
    numeroatleta = models.IntegerField('Nº do Atleta')
    datapresenca = models.DateField('Data da presença', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    # this is not needed if small_image is created at set_image
    def save(self, *args, **kwargs):
        atleta = Atleta.objects.get(pk=self.numeroatleta)
        self.nome = atleta.nome.title() + ' ' + atleta.sobrenome.title()
        super(Presenca, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Presenças'
        verbose_name = 'Presença'
        ordering = ('datapresenca',)

    def __str__(self):
        return str(self.numeroatleta)
