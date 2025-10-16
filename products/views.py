from .serializers import ProdcutSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer


    