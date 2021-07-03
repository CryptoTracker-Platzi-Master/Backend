from datetime import date
from django.db.models.aggregates import Avg ,Sum
from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.serializers import Serializer
from cryptos.serializer import CriptosSerializer, CriptosUserSerializer, InvestedSerializer, ProfitSerializar
from cryptos.models import Criptos
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import JsonResponse


def home(request):
    return HttpResponse("Welcome to the CryptotrackerAPI!")

class CriptosList(APIView):
    def get_object(self,pk):
        try:            
            return Criptos.objects.get(pk = pk)
        except Criptos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        criptos = self.get_object(pk)
        serializer = CriptosUserSerializer(criptos)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cripto = self.get_object(pk)
        serializer = CriptosSerializer(cripto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('update success')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        cripto = self.get_object(pk)
        serializer = CriptosSerializer(cripto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('delete success')
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request):        
        serializer = CriptosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Portfolio(generics.ListAPIView):
    serializer_class= CriptosUserSerializer

    def get_queryset(self):
        user = self.request.user
        criptos = Criptos.objects.filter(user_fk_id=self.request.user, able=1)
        return criptos

class ProfitPortfolio(generics.ListAPIView):
    serializer_class = ProfitSerializar

    def get_queryset(self):
        user = self.request.user
        criptos = Criptos.objects.filter(user_fk_id=self.request.user, able=1).order_by('id_c')[:1]
        return criptos

class AlgorithPortfolio(generics.ListAPIView):
    serializer_class= InvestedSerializer

    def get_queryset(self):
        s = 0
        user = self.request.user
        criptos = Criptos.objects.filter(user_fk_id=user, able=1)
        cr = len(criptos)
        ls = []
        for i in range(cr):
            ls.append(criptos[i].purchase_price)
        for i in ls:
            s += i
        return self.s



