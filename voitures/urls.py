from django.conf.urls import url
from clients import services

urlpatterns = [
    url(r'', services.client_list),
    url(r'/(?P<pk>[0-9]+)$', services.client_detail),
]
