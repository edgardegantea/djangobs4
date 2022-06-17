from django.db import models


# Create your models here.
class Website01(models.Model):
    nombre = models.CharField(verbose_name='elsoldemexico', max_length=150)
    url = models.URLField(verbose_name='https://www.elsoldemexico.com.mx/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Sitio web'
        verbose_name_plural = 'Sitios web'


class Website02(models.Model):
    nombre = models.CharField(verbose_name='elpais', max_length=150)
    url = models.URLField(verbose_name='hhttps://elpais.com/mexico/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Sitio web'
        verbose_name_plural = 'Sitios web'


class Website03(models.Model):
    nombre = models.CharField(verbose_name='milenio', max_length=150)
    url = models.URLField(verbose_name='https://www.milenio.com')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Sitio web'
        verbose_name_plural = 'Sitios web'

class Website04(models.Model):
    nombre = models.CharField(verbose_name='elfinanciero', max_length=150)
    url = models.URLField(verbose_name='https://www.elfinanciero.com.mx')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Sitio web'
        verbose_name_plural = 'Sitios web'
