from django.urls import path
from . import services

urlpatterns = [
    path('', services.reservation_list),
    path('<str:pk>/', services.reservation_detail),
    path('total-par-client/', services.reservation_total_par_client),  # optionnel
]
