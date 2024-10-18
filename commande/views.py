from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CommandeForm

from .models import Commande


@login_required(login_url='login')
def list_commande(request):
    commandes = Commande.objects.all()
    return render(request, 'commande/list.html', {'commandes': commandes})


@login_required(login_url='login')
def create(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, 'Commande crée avec success !')
            return redirect('/')
    context = {'form': form, 'content': f"Crée une nouvelle commande"}
    return render(request, 'commande/create.html', context)


@login_required(login_url='login')
def editer(request, pk):
    commande = get_object_or_404(Commande, id=pk)
    form = CommandeForm(instance=commande)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            messages.success(request, 'Commande mis a jour avec success !')

            return redirect('/')
    context = {'form': form, 'content': f"Editer {commande.nom}"}
    return render(request, 'commande/create.html', context)


@login_required(login_url='login')
def supprimer(request, pk):
    commande = get_object_or_404(Commande, id=pk)
    if request.method == 'POST':
        commande.delete()
        messages.success(request, 'Commande suprimé avec success !')

        return redirect('/')
    context = {'item': commande}
    return render(request, 'commande/supprimer.html', context)

@login_required(login_url='login')
def recevoir_commande(request, pk):
    commande = get_object_or_404(Commande, id=pk)
    return render(request, 'commande/recu.html', {'commande': commande})