from django.conf.urls import url, include
from django.contrib import admin
from kettclub.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^inscricao/', include('kettclub.subscriptions.urls',
                                namespace='subscriptions')),
    url(r'^presenca/', include('kettclub.assiduousness.urls',
                                namespace='assiduousness')),
    url(r'^admin/', admin.site.urls),
]
