from django.contrib.auth.models import User
from django.db import models
from django.forms import ChoiceField, RadioSelect

BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))


class Atleta(models.Model):
    planomensalidade = models.ForeignKey('PlanoMensalidade', verbose_name='Planos e mensalidade')
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

    class Meta:
        verbose_name_plural = 'Inscrições Atletas'
        verbose_name = 'Inscrição Atleta'
        ordering = ('nome',)

    def __str__(self):
        return str(self.pk)  # self.nome + ' ' + self.sobrenome


class PlanoMensalidade(models.Model):
    nome = models.CharField('Nome do plano', max_length=50)
    valor = models.DecimalField('Valor €', max_digits=5, decimal_places=2)
    horario = models.CharField('Horário', max_length=20)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Planos e mensalidade'
        verbose_name = 'Plano e mensalidade'
        ordering = ('valor',)

    def __str__(self):
        return self.nome + ' - ' + str(self.valor) + '€'


class SaudeAnamnese(models.Model):
    atleta = models.OneToOneField('Atleta', verbose_name='Nº do atleta')
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
        ordering = ('atleta__nome',)

    def __str__(self):
        return self.atleta.nome + ' ' + self.atleta.sobrenome


class Presenca(models.Model):
    numeroatleta = models.IntegerField('Nº do Atleta')
    datapresenca = models.DateField('Data da presença', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)



    class Meta:
        verbose_name_plural = 'Presenças'
        verbose_name = 'Presença'
        ordering = ('datapresenca',)

    def __str__(self):
        return str(self.numeroatleta)


class Avaliacao(models.Model):
    atleta = models.ForeignKey('Atleta', verbose_name='Nº do atleta')
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

    def __str__(self):
        return self.atleta.nome + ' ' + self.atleta.sobrenome
