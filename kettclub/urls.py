from django.conf.urls import url, include
from django.contrib import admin
from kettclub.administration.views import Logout, Login
from kettclub.core.views import home, success, unauthorized

admin.site.site_header = 'Administração Kettclub'

urlpatterns = [
    url(r'^$', home, name='home'),
    # url(r'^sucesso/', success, name='success'),
    url(r'^naoautorizada/$', unauthorized, name='redirect'),

    url(r'^administracao/', include('kettclub.administration.urls',
                                namespace='administration')),
    url(r'^login/', Login, name='login'),

    url(r'^logout/$', Logout, name='logout'),
    # url(r'^novo/', include('kettclub.subscriptions.urls',
    #                             namespace='subscriptions')),
    url(r'^inscricao/', include('kettclub.subscriptions.urls',
                                namespace='subscriptions')),
    url(r'^inscricaoexterna/', include('kettclub.externalapplication.urls',
                                namespace='external')),
    url(r'^presenca/', include('kettclub.assiduousness.urls',
                               namespace='assiduousness')),
    url(r'^avaliacaofisica/', include('kettclub.reviewsphysicals.urls',
                                      namespace='reviewsphysicals')),
    url(r'^planosmensais/', include('kettclub.monthlyplans.urls',
                                      namespace='monthlyplans')),
    url(r'^saudeanamnese/', include('kettclub.healthanamnese.urls',
                                    namespace='healthanamnese')),
    url(r'^config/', include('kettclub.config.urls',
                                    namespace='config')),
    url(r'^admin/', admin.site.urls),
]
