from contextlib import nullcontext
from email.policy import default
from random import choices
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
ESTADOS = [(1,'Reservado'),(2,'Completada'),(3,'Anulada'),(4,'No Asisten')]


class reserva(models.Model):
    nombreR=models.CharField(max_length=50)
    telefono=models.IntegerField()
    fechareserva = models.DateTimeField(auto_now_add=True)
    numeroPersonas = models.IntegerField(default=1, validators=[ MaxValueValidator(15), MinValueValidator(1) ])
    estado = models.IntegerField(
        null=False , blank=False,
        choices=ESTADOS,
        default=1

    )
    observacion = models.CharField(max_length=50,
        null=True, blank=True)
