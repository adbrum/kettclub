from django.conf.urls import url
from kettclub.externalapplication.views import new, success, empty_prototipo_form

urlpatterns = [
    url(r'^$', new, name='new'),
    # url(r'^edit/(?P<pk>\d+)$', editSubscription, name="edit"),
    url(r'^form/', empty_prototipo_form, name='form'),
    # url(r'^lista/', listsubscription, name='list'),
    # url(r'^deletar/', delDataModalSubscription, name='delete'),
    # url(r'^ativar/', activeDataModalSubscription, name='activate'),
    # url(r'^confirmedeletar/', delConfirmeSubscription, name='delconfirm'),
    # url(r'^confirmeativar/', activeConfirmeSubscription, name='activeconfirm'),
    url(r'^sucesso/', success, name='success'),
]
