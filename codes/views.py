from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from .serializer import CodeSerializer
from .models import Code


# Create your views here.

class CodeList(generics.ListAPIView):
    serializer_class = CodeSerializer
    def get_queryset(self):
        
        user = self.request.user
        return Code.objects.filter(user_id=user)
