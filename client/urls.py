from django.urls import path
from . import views

urlpatterns = [
    path('list_client/', views.list_client, name='list_client'),
    path('ajouter_client/', views.create, name='ajouter_client'),
    path('<str:pk>/', views.detail_client, name='client'),
    path('editer_client/<str:pk>', views.editer, name='editer_client'),
    path('supprimer_client/<str:pk>', views.supprimer, name='supprimer_client'),

]
