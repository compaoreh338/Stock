from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_commande, name='commande'),
    path('ajouter_commande/', views.create, name='ajouter_commande'),
    path('editer_commande/<str:pk>', views.editer, name='editer_commande'),
    path('supprimer_commande/<str:pk>', views.supprimer, name='supprimer_commande'),
    path('recu/<str:pk>', views.recevoir_commande, name='recevoir_commande'),

]
