from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='acceuil'),
    path('list_produit/', views.list, name='list_produit'),
    path('ajouter_produit/', views.create, name='ajouter_produit'),
    path('editer_produit/<str:pk>', views.editer, name='editer_produit'),
    path('supprimer_produit/<str:pk>', views.supprimer, name='supprimer_produit')

]
