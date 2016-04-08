from django.conf.urls import url
from kettclub.monthlyplans.views import new, editPlano, delDataModalPlano, \
    delConfirmePlano, listmonthlyplan, success, activeDataModalSubscription, activeConfirmeSubscription

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^edit/(?P<pk>\d+)$', editPlano, name="edit"),
    url(r'^lista/', listmonthlyplan, name='list'),
    url(r'^deletar/', delDataModalPlano, name='delete'),
    url(r'^ativar/', activeDataModalSubscription, name='activate'),
    url(r'^confirmedeletar/', delConfirmePlano, name='delconfirme'),
    url(r'^confirmeativar/', activeConfirmeSubscription, name='activeconfirm'),
    url(r'^sucesso/', success, name='success'),
]
