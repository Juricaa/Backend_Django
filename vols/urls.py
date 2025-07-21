from django.conf.urls import url
from voitures import services

urlpatterns = [
    url(r'', services.voiture_list),
    url(r'/(?P<pk>[0-9]+)$', services.voiture_detail),
]
