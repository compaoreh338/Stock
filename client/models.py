from django.db import models


class Client(models.Model):
    nom = models.CharField(max_length=200, blank=False, null=False)
    telephone = models.CharField(max_length=200, blank=False, null=False)  # Fixed typo in 'max_length'
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom}"
