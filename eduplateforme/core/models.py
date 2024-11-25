from django.contrib.auth.models import AbstractUser
from django.db import models

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
