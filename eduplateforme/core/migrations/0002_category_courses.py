# Generated by Django 5.1.3 on 2025-01-31 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nom de la catégorie')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/', verbose_name='Image de la catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre du cours')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Prix')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='Vidéo du cours')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/', verbose_name='Image illustration')),
                ('description', models.TextField(verbose_name='Description')),
                ('content', models.TextField(verbose_name='Contenu détaillé')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('status', models.CharField(default='active', max_length=20, verbose_name='Statut')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category', verbose_name='Catégorie')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Enseignant')),
            ],
        ),
    ]
