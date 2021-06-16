from django.http import HttpResponse
from rest_framework import viewsets
from .userSerializer import CriptosSerializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response


def home(request):
    return HttpResponse("Welcome to the CryptotrackerAPI!")

class CriptosList(APIView):
    def get(self, request):
        users = Criptos.objects.all()
        serializer = CriptosSerializer(users, many=True)
        return Response(serializer.data)