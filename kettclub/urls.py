from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import logout
from kettclub.core.views import home
from kettclub.administration.views import Logout, Login

admin.site.site_header = 'Administração Kettclub'

urlpatterns = [
    url(r'^$', home, name='home'),

    url(r'^administracao/', include('kettclub.administration.urls',
                                namespace='administration')),
    url(r'^login/', Login, name='login'),
    url(r'^logout/$', Logout, name='logout'),
    # url(r'^novo/', include('kettclub.subscriptions.urls',
    #                             namespace='subscriptions')),
    url(r'^inscricao/', include('kettclub.subscriptions.urls',
                                namespace='subscriptions')),
    url(r'^presenca/', include('kettclub.assiduousness.urls',
                               namespace='assiduousness')),
    url(r'^avaliacaofisica/', include('kettclub.reviewsphysicals.urls',
                                      namespace='reviewsphysical')),
    url(r'^planosmensais/', include('kettclub.monthlyplans.urls',
                                      namespace='monthlyplans')),
    url(r'^admin/', admin.site.urls),
]
