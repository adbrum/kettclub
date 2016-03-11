from django.conf.urls import url, include
from django.contrib import admin
from kettclub.core.views import home, dashboard

admin.site.site_header = 'Administração Kettclub'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^inscricao/', include('kettclub.subscriptions.urls',
                                namespace='subscriptions')),
    url(r'^presenca/', include('kettclub.assiduousness.urls',
                                namespace='assiduousness')),
    url(r'^avaliacaofisica/', include('kettclub.reviewsphysicals.urls',
                                namespace='reviewsphysical')),
    url(r'^admin/', admin.site.urls),
]
