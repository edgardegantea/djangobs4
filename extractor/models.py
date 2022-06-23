from django.db import models


# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    email = models.EmailField(verbose_name="Correo electrónico", max_length=100)
    telefono = models.CharField(verbose_name="Teléfono", max_length=20)
    mensaje = models.TextField(verbose_name="Mensaje")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Mensaje recibido"
        verbose_name_plural = "Mensajes recibidos"
