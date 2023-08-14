from django.db import models

# Create your models here.
class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    
    class Meta:
        verbose_name = 'categoria de productos'
        verbose_name_plural = "categorias de productos"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True,null=True, verbose_name="categoria")
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150, blank=True, null=True, verbose_name="descripcion")  
    precio = models.DecimalField(max_digits=10, decimal_places=2) 


    class meta:
        verbose_name = 'producto'
        verbose_name_plural = "productos"

    def __str__(self)-> str:
        return f'{self.nombre} ${self.precio: .2f}{self.categoria}, {self.descripcion}'