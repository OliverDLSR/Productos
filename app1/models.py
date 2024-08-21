from django.db import models

# Create your models here.
# app1/models.py

from django.db import models

class Producto(models.Model):
    TIPO_CHOICES = [
        ('local', 'Local'),
        ('internacional', 'Internacional'),
    ]
    
    codigo = models.CharField(max_length=20, unique=True, blank=True)
    nombre = models.CharField(max_length=100, default='Producto sin nombre')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=13, choices=TIPO_CHOICES)

    def save(self, *args, **kwargs):
        if not self.codigo:
            last_product = Producto.objects.all().order_by('id').last()
            if last_product:
                codigo_int = int(last_product.codigo) + 1
            else:
                codigo_int = 1
            self.codigo = f'{codigo_int:05d}'  # Esto generará un código con 5 dígitos, ej. 00001, 00002, etc.
        super().save(*args, **kwargs)

    def __str__(self):
        return self.codigo
