from rest_framework import serializers
from .models import *

class TiposDeCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposDeCuenta
        fields = '__all__'

class SistemasAuxiliaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = SistemasAuxiliares
        fields = '__all__'

class CuentasContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentasContable
        fields = '__all__'

class TiposDeMonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposDeMoneda
        fields = '__all__'

class EntradaContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntradaContable
        fields = '__all__'