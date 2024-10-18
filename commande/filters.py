import django_filters
from .models import Commande


class CommandeFilter(django_filters.FilterSet):
    class Meta:
        model = Commande
        fields = ['produit', 'status']
