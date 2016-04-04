from django.contrib import admin
from kettclub.assiduousness.models import Presenca
from kettclub.healthanamnese.models import SaudeAnamnese
from kettclub.monthlyplans.models import PlanoMensalidade
from kettclub.reviewsphysicals.models import Avaliacao
from kettclub.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'sobrenome', 'emailatleta', 'telefone', 'planomensalidade')
    fields = ('ativo', 'nome', 'sobrenome', 'emailatleta', 'datanascimento', 'idade', 'cc', 'nif', 'telefone', 'telefone2',
              'datainicio', 'planomensalidade')
    date_hierarchy = 'created_at'
    search_fields = ('nome', 'sobrenome', 'emailatleta', 'telefone', 'created_at')
    list_filter = ('created_at',)

    # Remove botão add
    def get_form(self, request, obj=None, **kwargs):  # Just added this override
        form = super(SubscriptionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['planomensalidade'].widget.can_add_related = False
        return form

    # Cria link no item do segundo campo da lista.
    def foo_link(self, obj):
        return u'<a href="/nome/%s/">%s</a>' % (obj.nome, obj)

    foo_link.allow_tags = True
    foo_link.short_description = "nome"

    def __init__(self, *args, **kwargs):
        super(SubscriptionAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('pk', 'nome')

    def pk(self, obj):
        nmatricula = Subscription.objects.get(pk=obj.pk)
        return str(nmatricula)

    pk.short_description = 'Nº Subscription'


class PlanoMensalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'horario', 'ativo')
    fields = ('nome', 'valor', 'horario', 'ativo')
    date_hierarchy = 'created_at'
    search_fields = ('nome', 'valor', 'horario', 'ativo', 'created_at')


class SaudeAnamneseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'atleta')
    fields = ('atleta',
              'quest01', 'quest02', 'quest03', 'quest04', 'quest05', 'quest06', 'quest07', 'quest08', 'quest09',
              'quest010', 'quest011', 'quest012', 'quest013', 'quest014', 'quest015', 'quest016', 'quest017',
              'quest018', 'quest019', 'quest020', 'quest021', 'quest022', 'quest023')
    date_hierarchy = 'created_at'
    search_fields = ('created_at',)
    # readonly_fields = ('atleta',)

    radio_fields = {"quest01": admin.HORIZONTAL, "quest02": admin.HORIZONTAL, "quest03": admin.HORIZONTAL,
                    "quest04": admin.HORIZONTAL, "quest05": admin.HORIZONTAL, "quest06": admin.HORIZONTAL,
                    "quest07": admin.HORIZONTAL, "quest08": admin.HORIZONTAL, "quest09": admin.HORIZONTAL,
                    "quest010": admin.HORIZONTAL, "quest011": admin.HORIZONTAL, "quest012": admin.HORIZONTAL,
                    "quest013": admin.HORIZONTAL, "quest014": admin.HORIZONTAL, "quest015": admin.HORIZONTAL,
                    "quest016": admin.HORIZONTAL, "quest017": admin.HORIZONTAL, "quest018": admin.HORIZONTAL,
                    "quest019": admin.HORIZONTAL, "quest020": admin.HORIZONTAL, "quest023": admin.HORIZONTAL}

    # Remove botão add
    def get_form(self, request, obj=None, **kwargs):  # Just added this override
        form = super(SaudeAnamneseAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['atleta'].widget.can_add_related = False
        return form

    def pk(self, obj):
        pk = Subscription.objects.get(pk=obj.pk)
        return pk.nome.title() + ' ' + pk.sobrenome.title()

    pk.short_description = 'Nome do atleta'


class PresencaAdmin(admin.ModelAdmin):
    app = 'kettclub.assiduousness'
    verbose_name = ('Assiduidade')
    list_display = ('numeroatleta', 'nome', 'datapresenca')
    fields = ('numeroatleta', 'datapresenca')
    date_hierarchy = 'created_at'
    search_fields = ('numeroatleta', 'datapresenca')
    list_filter = ('created_at',)

    # Cria link no item do segundo campo da lista.
    def foo_link(self, obj):
        return u'<a href="/nome/%s/">%s</a>' % (obj.nome, obj)

    foo_link.allow_tags = True
    foo_link.short_description = "numeroatleta"

    def __init__(self, *args, **kwargs):
        super(PresencaAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('nome', 'numeroatleta')

    # def pk(self, obj):
    #     pk = Subscription.objects.get(pk=obj.numeroatleta)
    #     return pk.nome.title() + ' ' + pk.sobrenome.title()
    #
    # pk.short_description = 'Nome do atleta'
    class Meta:
        varbose_app = 'Assiduidade do Subscription'


class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'dataavaliacao')
    # fields = ('numeroatleta', 'datapresenca')
    date_hierarchy = 'created_at'
    search_fields = ('atleta__nome', 'dataavaliacao')
    list_filter = ('created_at',)

    # Remove botão add
    def get_form(self, request, obj=None, **kwargs):  # Just added this override
        form = super(AvaliacaoAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['atleta'].widget.can_add_related = False
        return form


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(PlanoMensalidade, PlanoMensalidadeAdmin)
admin.site.register(SaudeAnamnese, SaudeAnamneseAdmin)
admin.site.register(Presenca, PresencaAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
