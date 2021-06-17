from rest_framework import serializers
from .models import Criptos
from django.contrib.auth.models import User
from auth.userSerializer import UserSerializer

class CriptosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Criptos        
        fields = '__all__'

class CriptosUserSerializer(serializers.ModelSerializer):
    user_fk_id = serializers.StringRelatedField()
    class Meta:
        model = Criptos        
        fields = '__all__'