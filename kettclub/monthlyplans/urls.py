from django.conf.urls import url
from kettclub.monthlyplans.views import new, editPlano, delDataModalPlano, \
    delConfirmePlano, listmonthlyplan

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^edit/(?P<pk>\d+)$', editPlano, name="editplano"),
    url(r'^lista/', listmonthlyplan, name='list'),
    url(r'^deletar/', delDataModalPlano, name='deletaratleta'),
    url(r'^confirmedeletar/', delConfirmePlano, name='delconfirme'),
]
