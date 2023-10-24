from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'tipodecuenta', views.TiposDeCuentaViewSet)
router.register(r'sistemasauxiliares', views.SistemasAuxiliaresViewSet)
router.register(r'cuentascontable', views.CuentasContableViewSet)
router.register(r'tiposdemoneda', views.TiposDeMonedaViewSet)
router.register(r'entradacontable', views.EntradaContableViewSet)

urlpatterns = [
    path('', include(router.urls))
]