from django.conf.urls import url

from kettclub.administration.views import dash, Logout, Login
from django.contrib.auth import views as auth_views
from kettclub.assiduousness.views import listassiduity
from kettclub.subscriptions.views import new, editAtleta, fichaAtleta, listsubscription, delDataModalAtleta, \
    delConfirmeAtleta

urlpatterns = [
    # url(r'^accounts/login/$', logindash, name='logindash'),
    # url(r'^accounts/login/$', auth_views.login),
    url(r'^login/', Login, name='login'),
    # url(r'^(?P<pk>\d+)/$', dash, name='dash'),
    url(r'^logout/', Logout, name='logout'),
    url(r'^$', dash, name='dash'),
    # url(r'^inscricao/', listinscription, name='inscription'),
    # url(r'^inscricao/$', new, name='new'),
    url(r'^edit/(?P<pk>\d+)$', editAtleta, name="editatleta"),
    # url(r'^delete/(?P<pk>\d+)$', deleteAtleta, name='delete'),
    url(r'^inscricao/', listsubscription, name='list'),
    url(r'^assiduidade/$', listassiduity, name='assiduidade'),
    url(r'^deletar/', delDataModalAtleta, name='deletaratleta'),
    url(r'^confirmedeletar/', delConfirmeAtleta, name='delconfirme'),

]
