from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
