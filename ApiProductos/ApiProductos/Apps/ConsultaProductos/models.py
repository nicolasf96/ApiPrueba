from django.db import models

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True,auto_created=True, null=False)
    nombre_producto = models.CharField(max_length=35, null=False)
    unidad_medida = models.CharField(max_length=20)
    tamaño = models.CharField(max_length=20)
    id_categoria = models.ForeignKey('Categorias', on_delete=models.CASCADE)

    def __unicode__(self):
        cadena = '{0} - {1}'.format(self.id_producto, self.nombre_producto)
        return cadena

class Producto_Precio(models.Model):
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    id_Precio = models.ForeignKey('Precio', on_delete=models.CASCADE)
    fecha_Precio_Desde = models.DecimalField(null=False,blank=False)

    def __unicode__(self):
        cadena = '{0} - Fecha: '.format(self.id_producto, self.fecha_Precio_Desde)
        return cadena

class Precio(models.Model):
    id_producto = models.IntegerField(primary_key=True,auto_created=True, null=False)
    precio = models.DecimalField(primary_key=True,null=False)

    def __unicode__(self):
        cadena = '{0} - ${1}'.format(self.id_producto, self.precio)
        return cadena

class Producto_Sucursal(models.Model):
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    id_sucursal = models.ForeignKey('Sucursal', null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    entrante = models.IntegerField(null=True)

    def __unicode__(self):
        cadena = '{0} - {1} - Stock: {2} '.format(self.id_producto, self.id_sucursal, self.stock)
        return cadena

class Sucursal(models.Model):
    id_sucursal = models.IntegerField(primary_key=True, auto_created=True, null=False)
    direccion = models.CharField(null=True)

    def __unicode__(self):
        cadena = '{0} - {1}'.format(self.id_sucursal, self.direccion)
        return cadena

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True,auto_created=True, null=False)
    nombre_categoria = models.CharField(null=False)

    def __unicode__(self):
        cadena = '{0} - {1}'.format(self.id_categoria, self.nombre_categoria)
        return cadena

class Empresa(models.Model):
    id_empresa = models.IntegerField(primary_key=True, auto_created=True, null=False)
    #FALTA TERMINAR

    def __unicode__(self):
        return self.id_empresa

