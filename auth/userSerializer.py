from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # criptos = serializers.PrimaryKeyRelatedField(many=True, queryset=Criptos.objects.all())

    class Meta:
        model = User
        fields = '__all__'