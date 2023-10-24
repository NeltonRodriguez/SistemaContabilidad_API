from rest_framework import viewsets
from .serializer import *
from .models import *

class TiposDeCuentaViewSet(viewsets.ModelViewSet):
    queryset = TiposDeCuenta.objects.all()
    serializer_class = TiposDeCuentaSerializer

class SistemasAuxiliaresViewSet(viewsets.ModelViewSet):
    queryset = SistemasAuxiliares.objects.all()
    serializer_class = SistemasAuxiliaresSerializer

class CuentasContableViewSet(viewsets.ModelViewSet):
    queryset = CuentasContable.objects.all()
    serializer_class = CuentasContableSerializer

class TiposDeMonedaViewSet(viewsets.ModelViewSet):
    queryset = TiposDeMoneda.objects.all()
    serializer_class = TiposDeMonedaSerializer

class EntradaContableViewSet(viewsets.ModelViewSet):
    queryset = EntradaContable.objects.all()
    serializer_class = EntradaContableSerializer

