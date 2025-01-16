from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'role', 'bio', 'profile_picture', 'date_of_birth', 'password1', 'password2']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'role',
            'bio',
            'profile_picture',
            'date_of_birth',
            'phone_number',
            'address',
            'institution',
            'grade',
        ]

    # Validation supplémentaire pour les champs personnalisés si nécessaire
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Un utilisateur avec cet email existe déjà.")
        return email

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth and date_of_birth > datetime.date.today():
            raise forms.ValidationError("La date de naissance ne peut pas être dans le futur.")
        return date_of_birth

    # Widgets pour un meilleur rendu des champs
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Parlez-nous de vous...',
            'rows': 3,
        }),
    )
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
        }),
    )
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
    )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex : +225 07 07 07 07 07',
        }),
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Votre adresse complète',
            'rows': 2,
        }),
    )
    institution = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom de votre établissement scolaire ou entreprise',
        }),
    )
    grade = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Niveau ou classe actuelle',
        }),
    )
    role = forms.ChoiceField(
        choices=User.ROLES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        required=True,
    )
