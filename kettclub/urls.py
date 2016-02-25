from django.conf.urls import url
from django.contrib import admin
from kettclub.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
]
