from django.db import models


class Tag(models.Model):
    nom = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    category_choices = [
        ('alimentaire', 'Alimentaire'),
        ('electronique', 'Electronique'),
        ('vetement', 'Vetement'),
        ('mobilier', 'Mobilier'),
        ('divers', 'Divers'),
    ]


    nom = models.CharField(max_length=200, blank=False, null=False)
    prix = models.FloatField(blank=False, null=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    categorie = models.CharField(max_length=200, choices=category_choices, default='alimentaire')
    tag = models.ManyToManyField(Tag)


    def __str__(self):
        return f"Produit: {self.nom}, Prix: {self.prix} , Categorie: {self.categorie}"
