from django.db import models

OPCIONES_ORIGEN = [
    ('Debito', 'Debito'),
    ('Credito', 'Credito'),
]

OPCIONES_ESTADO = [
    ('Disponible', 'Disponible'),
    ('No disponible', 'No disponible'),
]

OPCIONES_NIVEL = [
    (1, 'Nivel 1'),
    (2, 'Nivel 2'),
    (3, 'Nivel 3'),
]


class TiposDeCuenta(models.Model):
    descripcion = models.CharField(max_length=200, null=False)
    origen = models.CharField(max_length=10, choices=OPCIONES_ORIGEN, default='Debito')
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Disponible')
    
    def __str__(self):
        return self.descripcion

class SistemasAuxiliares(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Disponible')
    
    def __str__(self):
        return self.nombre

class CuentasContable(models.Model):
    descripcion = models.CharField(max_length=200, null=False)
    tipodecuenta = models.ForeignKey(TiposDeCuenta, on_delete=models.CASCADE)
    permite_transacciones = models.BooleanField(default=True)
    nivel = models.IntegerField(choices=OPCIONES_NIVEL, default=1)
    cuenta_mayor = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Disponible')
    
    def __str__(self):
        return self.descripcion

class TiposDeMoneda(models.Model):
    descripcion = models.CharField(max_length=200, null=False)
    ultima_tasa_cambiaria = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Disponible')
    
    def __str__(self):
        return self.descripcion

class EntradaContable(models.Model):
    descripcion = models.CharField(max_length=200, null=False)
    idAuxiliarOrigen = models.IntegerField()
    cuenta = models.CharField(max_length=30, null=False)
    tipo_movimiento = models.CharField(max_length=10, choices=OPCIONES_ORIGEN, default='Debito')
    fecha_asiento = models.DateTimeField(auto_now=True)
    monto_asiento = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Disponible')

    def __str__(self):
        return self.descripcion