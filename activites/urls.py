from django.urls import path
from activites import services


urlpatterns = [
    path('', services.activite_list, name='client-list'),
    path('<str:pk>/', services.activite_detail, name='client-detail'),
]
