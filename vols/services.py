from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser # type: ignore
from rest_framework import status # type: ignore
from rest_framework.decorators import api_view # type: ignore

from voitures.models import Voiture
from .serializers import ClientSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='post', request_body=ClientSerializer, responses={201: ClientSerializer})
@api_view(['GET', 'POST', 'DELETE'])
def voiture_list(request):
    if request.method == 'GET':
        voitures = Voiture.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            voitures = voitures.filter(name__icontains=name)

        serializer = ClientSerializer(voitures, many=True)
        return JsonResponse(
                {
                    'success': True,
                    'data': serializer.data
                 
                 },status=status.HTTP_200_OK)
       
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='put', request_body=ClientSerializer, operation_description="Met à jour un client")
@swagger_auto_schema(method='delete', operation_description="Supprime un client par ID")
@api_view(['GET', 'PUT', 'DELETE'])
def voiture_detail(request, pk):
    try:
        voiture = Voiture.objects.get(pk=pk)
    except Voiture.DoesNotExist:
        return JsonResponse({'message': 'Voiture not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(voiture)
        return JsonResponse(
                {
                    'success': True,
                    'data': serializer.data
                 
                 },status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClientSerializer(voiture, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        voiture.delete()
        return JsonResponse({'message': 'Voiture deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)