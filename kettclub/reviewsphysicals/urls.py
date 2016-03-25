from django.conf.urls import url
from kettclub.reviewsphysicals.views import new, editAvaliacao, listavaliacao, delDataModalAvaliacao, delConfirmeAvaliacao

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^edit/(?P<pk>\d+)$', editAvaliacao, name="editavaliacao"),
    url(r'^lista/', listavaliacao, name='list'),
    url(r'^deletar/', delDataModalAvaliacao, name='deletaravaliacao'),
    url(r'^confirmedeletar/', delConfirmeAvaliacao, name='delconfirme'),

]
