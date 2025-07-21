from rest_framework import serializers 
from activites.models import Activite 
 
 
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = '__all__'
