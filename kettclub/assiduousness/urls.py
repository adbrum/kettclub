from django.conf.urls import url
from kettclub.assiduousness.views import new, listassiduity


urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^lista/', listassiduity, name='list'),

]
