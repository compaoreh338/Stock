from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from commande.filters import CommandeFilter

from .forms import ClientForm
from .models import Client


@login_required(login_url='login')
def list_client(request):
    clients = Client.objects.annotate(commande_count=Count('commande'))
    context = {'clients': clients}
    return render(request, 'client/list.html', context)


@login_required(login_url='login')
def detail_client(request, pk):
    client = get_object_or_404(Client, id=pk)
    commandes = client.commande_set.all()  # Renamed to 'commandes' for clarity
    commande_total = commandes.count()
    myFilter = CommandeFilter(request.GET, queryset=commandes)
    commandes = myFilter.qs
    context = {'client': client, 'commandes': commandes, 'commande_total': commande_total, 'filter': myFilter}
    return render(request, 'client/detail.html', context)


@login_required(login_url='login')
def create(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client crée avec success!')
            return redirect('/')
    context = {'form': form, 'content': f"Crée nouveau client"}

    return render(request, 'client/create.html', context)


@login_required(login_url='login')
def editer(request, pk):
    client = get_object_or_404(Client, id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client mis a jour avec success !')
            return redirect('/')
    context = {'form': form, 'content': f"Editer {client.nom}"}
    return render(request, 'client/create.html', context)


@login_required(login_url='login')
def supprimer(request, pk):
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client suprimé avec success !');
        return redirect('/')
    context = {'item': client}
    return render(request, 'client/supprimer.html', context)
