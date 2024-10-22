from django.db import models
from client.models import Client
from produit.models import Produit


class Commande(models.Model):
    nom = models.CharField(max_length=200, blank=False, null=False)
    telephone = models.CharField(max_length=200, blank=False, null=False)  # Fixed typo in 'max_length'

    STATUS_CHOICES = [
        ('en instance', 'En instance'),
        ('non livré', 'Non livré'),
        ('livré', 'Livré'),
    ]
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    quantite = models.IntegerField(default=1)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='en instance')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"
