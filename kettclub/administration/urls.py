from django.conf.urls import url

from kettclub.administration.views import dash, Logout, Login

urlpatterns = [
    url(r'^login/', Login, name='login'),
    url(r'^logout/', Logout, name='logout'),
    url(r'^$', dash, name='dash'),
]
