from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre


class Operacion(models.Model):
    TIPO = [
        ('DEP', 'Depósito'),
        ('RET', 'Retiro'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='operaciones')
    tipo = models.CharField(max_length=3, choices=TIPO)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.monto}"