from rest_framework import serializers 
from .models import Facture, Client
# Dans factures/serializers.py
from clients.serializers import ClientSerializer  # Utilisez le même sérialiseur
 
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['idClient', 'name', 'email', 'destinations'] 
        ref_name = 'ClientSerializer_FacturesApp'

class FactureSerializer(serializers.ModelSerializer):
    clientId = ClientSerializer(read_only=True)

    class Meta:
        model = Facture
        fields = '__all__'

class FactureSerializerCreated(serializers.ModelSerializer):

    class Meta:
        model = Facture
        fields = '__all__'
