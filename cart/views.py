from .serializers import CartItemSerializer
from rest_framework import viewsets
from .models import CartItem



class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
