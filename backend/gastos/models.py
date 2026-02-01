from django.db import models
from django.contrib.auth.models import User

fuentes = [
    ('Efectivo', 'Efectivo'),
    ('Tarjeta Débito', 'Tarjeta Débito'),
    ('Tarjeta Crédito', 'Tarjeta Crédito'),
    ('Transferencia', 'Transferencia'),
    ('Otro', 'Otro'),]


class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Gastos(models.Model):
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    soporte = models.ImageField(upload_to='soportes/', blank=True, null=True)
    fuente_pago = models.CharField(
        max_length=20,
        choices=fuentes,
        default='Efectivo'
    )
    # usuario_creador = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='gastos'
    # )
    categoria = models.ForeignKey(
        Categorias,
        on_delete=models.CASCADE,
        related_name='gastos'
    )
    def __str__(self):
        return f'{self.descripcion} - {self.total}'

class GastosItems(models.Model):
    gasto = models.ForeignKey(
        Gastos,
        on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=3)

    def __str__(self):
        return f'id:{self.gasto} - item:{self.nombre} - cantidad:{self.cantidad} - precio:{self.precio_unitario}'