from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.name} ({self.price})'


class Order(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    products = models.ManyToManyField(
        Product,
        through='OrderPosition',
        related_name='orders',
    )


class OrderPosition(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    quantity = models.PositiveIntegerField()
