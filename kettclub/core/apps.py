from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'kettclub.core'
    verbose_name = 'Administração Kettclub'


class SubscriptionsConfig(AppConfig):
    name = 'kettclub.subscriptions'
    verbose_name = 'Inscrições atletas'


class AssiduousnessConfig(AppConfig):
    name = 'kettclub.assiduousness'
    verbose_name = 'Assiduidade'


class HealthanamneseConfig(AppConfig):
    name = 'kettclub.healthanamnese'
    verbose_name = 'Saude e Anamnese'


class MonthlyplansConfig(AppConfig):
    name = 'kettclub.monthlyplans'
    verbose_name = 'Planos mensais'
