from django.http.response import HttpResponse
from rest_framework import serializers
from .models import Criptos
from django.contrib.auth.models import User
from auth.userSerializer import UserSerializer
from datetime import date, datetime
from django.db.models import Sum, Avg, Count, F, Value


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

class PurchseProfitSerializar(serializers.ModelSerializer):

    
    class Meta:
        model = Criptos
        fields = '__all__'
    

    def to_representation(self, instance):
        s_pur_price = Criptos.objects.aggregate(purchase_price=Sum('purchase_price'))
        s_take_profit = Criptos.objects.aggregate(total_profit=Sum('take_profit'))
        total_profit = Criptos.objects.aggregate(expected_earnings=Sum(F('take_profit')-F('purchase_price')))
        
        # return criptos
        return {            
            'purchase_price': s_pur_price,
            'take_profit': s_take_profit,
            'excepted_earnings':total_profit,
        }
        