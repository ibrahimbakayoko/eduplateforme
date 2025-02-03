from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    # Rôles possibles pour les utilisateurs
    STUDENT = 'student'
    TEACHER = 'teacher'
    ADMIN = 'admin'
    ROLES = [
        (STUDENT, 'Étudiant'),
        (TEACHER, 'Enseignant'),
        (ADMIN, 'Administrateur'),
    ]

    # Champs personnalisés
    email = models.EmailField(unique=True)  # Email obligatoire et unique
    role = models.CharField(max_length=10, choices=ROLES, default=STUDENT)
    bio = models.TextField(blank=True, null=True)  # Description personnelle
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)  # Photo de profil
    date_of_birth = models.DateField(blank=True, null=True)  # Date de naissance

    # Informations générales
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Numéro de téléphone
    address = models.TextField(blank=True, null=True)  # Adresse
    date_joined = models.DateTimeField(auto_now_add=True)  # Date d'inscription
    is_active = models.BooleanField(default=True)  # Statut actif/inactif

    # Champs spécifiques
    # Exemples pour une plateforme éducative
    institution = models.CharField(max_length=100, blank=True, null=True)  # Établissement scolaire ou entreprise
    grade = models.CharField(max_length=50, blank=True, null=True)  # Classe ou niveau pour les étudiants

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    




# class Course(models.Model):
#     title = models.CharField(max_length=200, verbose_name="Titre du cours")
#     description = models.TextField(verbose_name="Description")
#     instructor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Enseignant")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
#     def __str__(self):
#         return self.title




class Courses(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre du cours")
    image = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name="Image illustration")
    description = models.TextField(verbose_name="Description")
    content = models.TextField(verbose_name="Contenu détaillé")
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Enseignant")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    status = models.CharField(max_length=20, default='active', verbose_name="Statut")  # Nouveau champ
    

    def __str__(self):
        return self.title
    





