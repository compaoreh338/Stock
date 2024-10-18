from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.inscriptionPagre, name='inscription'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('editer/', views.edit_profile, name='editer_profile'),
    path('password/', views.change_password, name='change_password'),
    path('<str:pk>/password/', views.change_password_with_pk),



]
