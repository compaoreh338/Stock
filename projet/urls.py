from django.contrib import admin
from django.urls import path, include
from compte.views import change_password_with_pk

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produit.urls')),
    path('client/', include('client.urls')),
    path('commande/', include('commande.urls')),
    path('compte/', include('compte.urls')),
    path('<int:pk>/password/', change_password_with_pk),

]
