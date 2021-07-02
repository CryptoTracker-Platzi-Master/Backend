from rest_framework import serializers
from .models import Criptos
from django.contrib.auth.models import User
from auth.userSerializer import UserSerializer
from datetime import datetime


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
            'id_c': instance.id_c,
            'username': instance.user_fk.username,
            'name': instance.name,
            'symbol': instance.symbol,
            'purchase_price': instance.purchase_price,
            'amount_invested': instance.amount_invested,
            'take_profit': instance.take_profit,
            'stop_loss': instance.stop_loss,
            'cantity': instance.cantity,
        }