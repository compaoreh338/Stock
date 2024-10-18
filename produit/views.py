from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from client.models import Client
from commande.models import Commande
from .forms import ProduitForm
from .models import Produit


@login_required(login_url='login')
def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    produits = Produit.objects.all()
    context = {'commandes': commandes, 'clients': clients ,'produits': produits}
    return render(request, 'produit/acceuil.html', context)


@login_required(login_url='login')
def list(request):
    produits = Produit.objects.all()
    context = {'produits': produits}
    return render(request, 'produit/list.html', context)


@login_required(login_url='login')
def create(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit crée avec success !')
            return redirect('/')
    context = {'form': form, 'content': f"Crée un nouveau produit"}
    return render(request, 'produit/create.html', context)


@login_required(login_url='login')
def editer(request, pk):
    produit = get_object_or_404(Produit, id=pk)
    form = ProduitForm(instance=produit)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit mis a jour avec success !')

            return redirect('/')
    context = {'form': form,'content': f"Editer {produit.nom}"}
    return render(request, 'produit/create.html', context)


@login_required(login_url='login')
def supprimer(request, pk):
    produit = get_object_or_404(Produit, id=pk)
    if request.method == 'POST':
        produit.delete()
        messages.success(request, 'Produit supprimé avec success !')

        return redirect('/')
    context = {'item': produit}
    return render(request, 'produit/supprimer.html', context)
