from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Courses
#from .models import Article



#Vue pour la home
def home(request):
    last_courses= Courses.objects.order_by('created_at')[:3]
    return render(request, 'core/home.html',{
        'last_courses':last_courses,
    })

# Vue pour l'inscription
# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Connecte l'utilisateur après l'inscription
#             messages.success(request, "Compte créé avec succès !")
#             return redirect('home')  # Remplacer 'home' par l'URL vers la page d'accueil
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'core/signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Compte créé avec succès !")
            return redirect('home')
        else:
            # Débogage : Affiche les erreurs dans la console
            print("Erreurs dans le formulaire :", form.errors)
            
            # Ajouter un message générique pour les utilisateurs
            messages.error(request, "Une erreur est survenue. Veuillez vérifier vos informations.")
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


# Vue pour les cours
def course_list(request):
    courses = Courses.objects.all()
    return render(request, 'core/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = Courses.objects.get(id=course_id)
    return render(request, 'core/course_detail.html', {'course': course})


