from django.db import models
from django.urls import reverse

# Create your models here.
class pacientes1(models.Model):
    nombre=models.CharField(max_length=50)
    apellidoP=models.CharField(max_length=30)
    apellidoM=models.CharField(max_length=30)
    Fecha_na=models.DateField(null=True, blank=True)
    image=models.ImageField(upload_to='pacientes_imagen/',blank=True, null=True)
    def get_absolute_url(self):
        """
        Retonar la Url para acceder a una instancia particular de un paciente
        """
        return reverse('paciente-detalle', args=[str(self.id)])
    def __str__(self):

        return '%s %s' % (self.nombre, self.apellidoP)

#tabla para documentos
class documentos(models.Model):
    NomFile=models.CharField(max_length=100)
    file=models.FileField(upload_to='archivos/pacientes', blank=True, null=True)
    paciente=models.ForeignKey('pacientes1', on_delete=models.CASCADE, null=True)
    fecha_subida=models.DateField(auto_now_add=True)

    class Meta:
        ordering=["fecha_subida"]
    
    def __str__(self):

        return '%s %s' % (self.id,self.NomFile)

#tabla para usuarios
#class user(models.Model):

