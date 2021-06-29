from codes.models import Code
from auth.userSerializer import UserSerializer
from rest_framework import serializers

class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = '__all__'