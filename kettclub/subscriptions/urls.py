from django.conf.urls import url
from kettclub.subscriptions.views import new, listsubscription, empty_prototipo_form, editAtleta, delDataModalAtleta, \
    delConfirmeAtleta

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^edit/(?P<pk>\d+)$', editAtleta, name="editatleta"),
    url(r'^form/', empty_prototipo_form, name='form'),
    url(r'^lista/', listsubscription, name='list'),
    url(r'^deletar/', delDataModalAtleta, name='deletaratleta'),
    url(r'^confirmedeletar/', delConfirmeAtleta, name='delconfirme'),
]
