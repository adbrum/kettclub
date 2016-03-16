from django.conf.urls import url
from kettclub.dashboard.views import dash, Logout, Login
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^accounts/login/$', logindash, name='logindash'),
    # url(r'^accounts/login/$', auth_views.login),
    # url(r'^login/', Login, name='login'),
    # url(r'^(?P<pk>\d+)/$', dash, name='dash'),
    # url(r'^logout/', Logout, name='logout'),
    url(r'^$', dash, name='dash'),


]
