from django.db import models
#from django.contrib.auth.models import User

"""
# Profile User.
class Profile(models.Model):

# Option Choose Faculty
    FACULTY_CHOICES = (
        ('Ingenieria Sistemas', 'Ingenieria_sistemas'),
        ('Ingenieria civil', 'Ingenieria_civil'),
        ('Derecho', 'Derecho'),
        ('Psicologia', 'Psicologia'),
        ('Medicina Veterinaria y Zootecnia', 'Veterinaria'),
        ('Contaduría Pública', 'Contaduría_publica'),
        ('Enfermería profesional', 'Enfermeria_profesional'),
        ('Medicina', 'Medicina'),
        ('Odontología', 'Odontologia'),
    )

# Create Tables Profile

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name='imagen')
    name = models.CharField(max_length=255, null=True, blank=True,  verbose_name='nombre')
    lastName = models.CharField(max_length=255, null=True, blank=True, verbose_name='apellido')
    idU = models.CharField(max_length=6, verbose_name='id_Universidad')
    faculty = models.CharField(max_length=50, verbose_name='Facultad', choices=FACULTY_CHOICES)
    email_campus = models.EmailField(max_length=50, verbose_name='Correo CampusUcc')
    phone_number = models.CharField(max_length=10, verbose_name='Numero de Telefono')
"""

# Create your groups here.
"""
estudiante_group = Group.objects.create(name='Estudiante')
admin_bienestar_group = Group.objects.create(name='Admin Bienestar')
staff_group = Group.objects.create(name='Staff')
"""