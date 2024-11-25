from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages



#Vue pour la home
def home(request):
    return render(request, 'core/home.html')

# Vue pour l'inscription
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte l'utilisateur après l'inscription
            messages.success(request, "Compte créé avec succès !")
            return redirect('home')  # Remplacer 'home' par l'URL vers la page d'accueil
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

# Vue pour la connexion
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenue, {user.username}!")
            return redirect('home')  # Remplacer 'home' par l'URL vers la page d'accueil
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})
