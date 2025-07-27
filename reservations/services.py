from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.contenttypes.models import ContentType
from drf_yasg.utils import swagger_auto_schema
from .models import Reservation
from .serializers import ReservationSerializer
from clients.models import Client

@swagger_auto_schema(method='post', request_body=ReservationSerializer)
@api_view(['GET', 'POST'])
def reservation_list(request):
    if request.method == 'GET':
        reservations = Reservation.objects.select_related('id_client')
        serializer = ReservationSerializer(reservations, many=True)
        return JsonResponse({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=ReservationSerializer)
@swagger_auto_schema(method='delete')
@api_view(['GET', 'PUT', 'DELETE'])
def reservation_detail(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return JsonResponse({'message': 'Réservation introuvable'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservationSerializer(reservation)
        return JsonResponse({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        # Calcul du montant
        from datetime import datetime
        date_debut = datetime.strptime(data['date_debut'], '%Y-%m-%d').date()
        date_fin = datetime.strptime(data['date_fin'], '%Y-%m-%d').date()
        quantite = int(data.get('quantite', 1))
        nb_jours = (date_fin - date_debut).days
        montant = nb_jours * quantite
        data['montant'] = montant

        serializer = ReservationSerializer(reservation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reservation.delete()
        return JsonResponse({'message': 'Réservation supprimée'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def reservation_total_par_client(request):
    data = []
    clients = Client.objects.all()
    for client in clients:
        reservations = Reservation.objects.filter(client=client)
        total = sum([res.montant for res in reservations])
        data.append({
            'client': f"{client.nom} {client.prenom}",
            'total_reservations': len(reservations),
            'montant_total': total
        })
    return JsonResponse({'success': True, 'data': data}, status=200)
