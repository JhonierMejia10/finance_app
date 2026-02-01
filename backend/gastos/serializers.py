from rest_framework import serializers
from .models import Categorias, Gastos, GastosItems

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['nombre','descripcion']

class GastosItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GastosItems
        fields = '__all__'

#creacion de gastos con items
class GastosItemsCreateSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=False)
    cantidad = serializers.IntegerField(min_value=1)
    precio_unitario = serializers.DecimalField(
        max_digits=12,
        decimal_places=3,
        min_value=0.1
    )
#Creacion de gastos con items
class GastosSerializer(serializers.ModelSerializer):
    items = GastosItemsCreateSerializer(many=True, required=False)
    class Meta:
        model = Gastos
        fields = [
            'fecha',
            'descripcion',
            'total',
            'soporte',
            'fuente_pago',
            'categoria',
            'items'
        ]