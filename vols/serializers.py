from rest_framework import serializers 
from voitures.models import Voiture  
 
 
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = '__all__'
