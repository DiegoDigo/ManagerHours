from __future__ import unicode_literals
from django.db import models


class Veicle(models.Model):
    name_line = models.CharField('nome linha', max_length =150)
    numer_line = models.IntegerField('Numero da linha')
    numer_car = models.CharField('numero carro', max_length=5)

    def __str__(self):
        return self.name_line

    class Meta:
        verbose_name_plural = 'Veicles'
        verbose_name = 'Veicles'