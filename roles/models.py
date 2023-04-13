from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import Group

# Profile User.

class Profile(models.Model):

# Option Choose
    FACULTY_CHOICES = (
        ('Ingenieria sistemas', 'Ingenieria sistemas'),
        ('Ingenieria civil', 'Ingenieria civil'),
        ('Derecho', 'Derecho'),
        ('Psicologia', 'Psicologia'),
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name='imagen')
    name = models.CharField(max_length=255, null=True, blank=True,  verbose_name='nombre')
    lastName = models.CharField(max_length=255, null=True, blank=True, verbose_name='apellido')
    idU = models.CharField(max_length=6, verbose_name='id_Universidad')
    faculty = models.CharField(max_length=50, verbose_name='Facultad', choices=FACULTY_CHOICES)



# Create your groups here.
"""
estudiante_group = Group.objects.create(name='Estudiante')
admin_bienestar_group = Group.objects.create(name='Admin Bienestar')
staff_group = Group.objects.create(name='Staff')
"""