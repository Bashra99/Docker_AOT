from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

from .models import AOT
from .serializers import AOTSerializer
# Create your views here.

class AOTListView(ListCreateAPIView):
    queryset = AOT.objects.all()
    serializer_class= AOTSerializer


# class AOTCreateView(ListCreateAPIView):
#     queryset = AOT.objects.all()
#     serializer_class= AOTSerializer

class AOTDetailView(RetrieveUpdateDestroyAPIView):
    queryset = AOT.objects.all()
    serializer_class= AOTSerializer


