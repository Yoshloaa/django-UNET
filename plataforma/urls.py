from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('registro_usuarios/', views.registrar_usuario, name='registar_usuario'),
    path('principal/',views.index, name='principal'),
    path('cerrar/',views.cerrar_sesion,name='logout'),
    path('login/',views.iniciarSession ,name='login'),
    path('pacientes/',views.pacientes, name='pacientes'),
    path('pacientes/crear/',views.crear_paciente, name='crear_pacientes'),
    path('pacientes/<int:paciente_id>/',views.mostrar_paciente, name='mostrar_pacientes'),
    path('pacientes/<int:paciente_id>/actualizar/',views.actualizar_paciente,name='actualizar paciente'),
    
    path('agendas/',views.agendas,name='agendas'),
    #path('',views,name=''),
    #path('',views,name=''),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)