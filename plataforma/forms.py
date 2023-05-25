from django.forms import ModelForm
from .models import pacientes1 ,documentos

class busquedaP(ModelForm):
    class Meta:
        model = pacientes1
        fields= ['nombre']

class CreacionP(ModelForm):
    class Meta:
        model= pacientes1
        fields=['image','nombre', 'apellidoP', 'apellidoM','Fecha_na']
#class subirDoc(ModelForm):
 #   class Meta:
   #     model = documentos
        