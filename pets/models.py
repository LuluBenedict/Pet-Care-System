from django.db import models
from client.models import Client

class Pet(models.Model):

    SPECIES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Rabbit', 'Rabbit'),
        ('Other', 'Other'),
    ]

    owner = models.ForeignKey(Client, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=SPECIES)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name