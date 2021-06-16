from rest_framework import serializers
from .models import Criptos



class CriptosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Criptos        
        fields = '__all__'