from django.db import models
from django.contrib.auth.models import User
from cart.models import CartItem


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10 , choices=[('pending', 'Pending'), ('shipped', 'Shipped')])
    created_at = models.DateTimeField(auto_now_add=True)


    