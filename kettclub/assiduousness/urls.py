from django.conf.urls import url
from kettclub.assiduousness.views import new

urlpatterns = [
    url(r'^$', new, name='new'),

]
