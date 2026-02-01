from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Gastos, GastosItems

class GastoService:

    @staticmethod
    @transaction.atomic
    def crear_gasto_service(items,categoria,fuente_pago,total,descripcion=None,soporte=None):

        if not items or len(items)== 0:
            raise ValidationError("Debe incluir al menos un item a su gasto.")
        
        try:
            gasto = Gastos.objects.create(
                descripcion = descripcion,
                categoria = categoria,
                fuente_pago = fuente_pago,
                soporte = soporte,
                total = total
            )
        except Exception as e:
            raise ValidationError(f"No se pudo crear el gasto: {str(e)}" )
        
        for item in items:
            nombre = item['nombre']
            cantidad = item['cantidad']
            precio_unitario = item['precio_unitario']

            try:
                GastosItems.objects.create(
                    gasto = gasto,
                    nombre = nombre,
                    cantidad = cantidad,
                    precio_unitario = precio_unitario
                )
            except Exception as e:
                raise ValidationError(f"Error al registrar un item de gasto {str(e)}")
            
        return gasto
        
     