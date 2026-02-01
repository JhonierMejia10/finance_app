from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GastosSerializer, CategoriaSerializer, GastosItemsSerializer
from .models import Gastos, Categorias, GastosItems
from rest_framework.permissions import AllowAny
from .service import GastoService
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.response import Response


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]

class GastosViewSet(viewsets.ModelViewSet):
    queryset = Gastos.objects.all()
    serializer_class = GastosSerializer
    permission_classes = [AllowAny]
        
    def create(self, request, *args, **kwargs):
        serializer = GastosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            gasto = GastoService.crear_gasto_service(
                items=data.get('items'),  # 👈 AQUÍ ESTABA EL ERROR
                descripcion=data.get('descripcion'),
                total=data['total'],
                soporte=data.get('soporte'),
                fuente_pago=data['fuente_pago'],
                categoria=data['categoria']
            )

            return Response(
                {
                    'status': True,
                    'message': 'Gasto creado correctamente',
                    'id': gasto.id
                },
                status=status.HTTP_201_CREATED
            )

        except ValidationError as e:
            return Response(
                {
                    'status': False,
                    'message': 'El gasto no ha podido ser insertado.',
                    'detail': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        gasto_serializer = GastosSerializer(gasto)
        return Response(gasto_serializer.data, status=status.HTTP_201_CREATED)


class GastosItemsViewSet(viewsets.ModelViewSet):
    queryset = GastosItems.objects.all()
    serializer_class = GastosItemsSerializer
    permission_classes = [AllowAny]