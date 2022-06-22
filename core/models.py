from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.


class Usuario(models.Model):

    nombre = models.CharField(max_length= 70, verbose_name ='Nombre')
    apellido= models.CharField(max_length= 70, verbose_name ='Apellido')
    rut = models.CharField(max_length=10, primary_key=True, verbose_name ='Rut')
    telefono = models.CharField(max_length= 10, verbose_name ='Telefono')
    correo = models.CharField(max_length= 40, verbose_name ='Correo')
    password = models.CharField(max_length= 8, verbose_name ='password')

    def __str__(self):
       return self.rut

class Contacto(models.Model):

    auto_increment_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 70, verbose_name ='Nombre')
    apellido= models.CharField(max_length= 70, verbose_name ='Apellido')
    rut = models.CharField(max_length=10, verbose_name ='Rut')
    telefono = models.CharField(max_length= 10, verbose_name ='Telefono')
    correo = models.CharField(max_length= 40, verbose_name ='Correo')
    comentario = models.CharField(max_length= 500, verbose_name ='Comentario')

    def __str__(self):
       return self.auto_increment_id





