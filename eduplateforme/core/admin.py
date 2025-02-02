from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .models import Courses
from .models import Category
#from .models import Article

# Configuration de l'affichage du modèle utilisateur personnalisé dans l'interface d'administration
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Champs à afficher dans la liste des utilisateurs
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    
    # Champs en lecture seule
    readonly_fields = ('date_joined',)
    
    # Champs à afficher dans le formulaire d'édition
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'bio', 'profile_picture')}),
        ('Rôles et permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Informations supplémentaires', {'fields': ('phone_number', 'address', 'institution', 'grade', 'date_joined')}),
    )
    
    # Champs à afficher dans le formulaire de création
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role'),
        }),
    )

    
    # Champs à utiliser pour la recherche
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(Courses)
admin.site.register(Category)
# ajout du model article
#admin.site.register(Article)

