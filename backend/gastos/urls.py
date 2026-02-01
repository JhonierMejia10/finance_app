from django.urls import path, include
from .views import GastosViewSet, CategoriasViewSet, GastosItemsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'gastos', GastosViewSet, basename='gastos')
router.register(r'categorias', CategoriasViewSet, basename='categorias')
router.register(r'gastos-items', GastosItemsViewSet, basename='gastos-items')

urlpatterns = [
    path('', include(router.urls))  
]
