from rest_framework import serializers 
from activites.models import Activite 
 
 
class ActiviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = '__all__'
