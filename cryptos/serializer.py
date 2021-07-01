from rest_framework import serializers
from .models import Criptos
from django.contrib.auth.models import User
from auth.userSerializer import UserSerializer
from datetime import datetime
from django.db.models import Sum, Avg

class CriptosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Criptos        
        fields = '__all__'
    

class CriptosUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Criptos
        fields = '__all__'
    
    def to_representation(self, instance):

        return{
            'id': instance.id_c,
            'username': instance.user_fk.username,
            'name': instance.name,
            'symbol': instance.symbol,
            'purchase_price': instance.purchase_price,
            'take_profit': instance.take_profit,
            'stop_loss': instance.stop_loss,
            'cantity': instance.cantity,
        }


class AlgorithmsCriptosUserSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Criptos
        fields = '__all__'
    

    def to_representation(self, instance):
        criptos = Criptos.objects.aggregate(total_purchase=Sum('purchase_price'))
        return criptos
        # return{            
        #     'purchase_price': criptos
        # }

    