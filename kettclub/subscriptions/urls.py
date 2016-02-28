from django.conf.urls import url
from kettclub.subscriptions.views import new

urlpatterns = [
    url(r'^$', new, name='new'),

]
