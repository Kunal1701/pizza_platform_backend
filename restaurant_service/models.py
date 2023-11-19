from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    is_online = models.BooleanField(default=False)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    pizza = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)