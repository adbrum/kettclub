from django.conf.urls import url

from kettclub.administration.views import dash, Logout, Login
from django.contrib.auth import views as auth_views
from kettclub.assiduousness.views import listassiduity
from kettclub.subscriptions.views import new, editAtleta, fichaAtleta, listsubscription, delDataModalAtleta, \
    delConfirmeAtleta

urlpatterns = [
    url(r'^login/', Login, name='login'),
    url(r'^logout/', Logout, name='logout'),
    url(r'^$', dash, name='dash'),
]
