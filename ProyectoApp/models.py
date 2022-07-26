from django.db import models

class Turismo(models.Model):
    codigo= models.CharField(primary_key=True, max_length=6)
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=900)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Turismo'
        verbose_name_plural = 'Turismos'
    def __str__(self):
        return f'{self.codigo} : {self.titulo}'
# Creacion de mi usuario con : Super Usuario:
#  User :MiguelTorres123 
# Contraseña : miguel123