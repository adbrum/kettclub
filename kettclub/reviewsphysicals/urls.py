from django.conf.urls import url
from kettclub.reviewsphysicals.views import new

urlpatterns = [
    url(r'^$', new, name='new'),

]
