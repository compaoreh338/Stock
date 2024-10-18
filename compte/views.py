from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.models import User

from .forms import InscriptionForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.

def inscriptionPagre(request):
    form = InscriptionForm(request.POST)
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Utulisateur } crée avec success!')
            return redirect('login')
    context = {'form': form}
    return render(request, 'compte/inscription.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Vous etes connecté en tant que {user.username} !')

            return redirect('acceuil')
        else:
            messages.info(request, 'Il y a une erreur')

    return render(request, 'compte/login.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)

    return redirect('login')


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('acceuil')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'compte/editer.html', {'form': form})


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            logout(request)
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')  # Redirect to a success page
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'compte/change_password.html', {'form': form})

@login_required(login_url='login')
def change_password_with_pk(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)  # Pass the user directly
        if form.is_valid():
            user = form.save()
            logout(request)
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')  # Redirect to a success page
    else:
        form = PasswordChangeForm(user)  # Use the user here for the form

    return render(request, 'compte/change_password.html', {'form': form})