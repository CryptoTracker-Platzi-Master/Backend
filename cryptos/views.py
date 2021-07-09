from datetime import date
from django.db.models.aggregates import Avg ,Sum
from django.db.models import Case ,When
from django.db.models.fields import DecimalField
from django.db.models.query import QuerySet
from django.utils.functional import Promise
from rest_framework import serializers
from rest_framework.serializers import Serializer
from cryptos.serializer import CriptosSerializer, CriptosUserSerializer
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
        c=float(request.data['cantity'])
        p=float(request.data['purchase_price'])
        total_invested = c*p
        data_custom = request.data
        data_custom['able'] = 1
        data_custom['total_invested'] = total_invested
        cripto = self.get_object(pk)
        serializer = CriptosSerializer(cripto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('update success')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        cripto = self.get_object(pk)
        if cripto:
            cripto.able = 0
            cripto.save()
            return Response(
                {
                    "message": "delete success"
                },
                status=status.HTTP_200_OK
            )
        return Response({"error": "The Activity not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        c=float(request.data['cantity'])
        p=float(request.data['purchase_price'])
        total_invested = c*p
        data_custom = request.data
        data_custom['total_invested'] = total_invested
        # print(data_custom)
        serializer = CriptosSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Portfolio(generics.RetrieveAPIView):
    serializer_class= CriptosUserSerializer
    # def get_queryset(self):
    # def retrieve(self, request, *args, **kwargs):
    def retrieve(self,request):
        user = self.request.user
        criptos = Criptos.objects.filter(user_fk_id=user, able=1)
        suma_total_invested = Criptos.objects.filter(user_fk=user, able=1).aggregate(Sum('total_invested'))
        
        data = {
            "sum": suma_total_invested,            
            "criptos" : criptos.values()
        }
        return Response(data)
