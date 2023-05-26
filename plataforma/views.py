from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login , logout, authenticate
from django.db import IntegrityError
from .models import pacientes1,documentos
from django.http import HttpResponse
from .forms import busquedaP,CreacionP

# Create your views here.
#pagina principal

def index(request):
    return render(request,'index.html')
#registrar usuarios
def registrar_usuario(request):
    if request.method == 'GET':
        return render(request,'registroU.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user= User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('principal')

            except IntegrityError:
                return render(request,'registroU.html',{
                    'form':UserCreationForm,
                    "error":'usuario ya existe'})
            
        return render(request,'registroU.html',{
                    'form':UserCreationForm,
                    "error":'el password no coicide'})
#iniciar y cerrar session
def cerrar_sesion(request):
    logout(request)
    return redirect('home')         

def iniciarSession(request):
       if request.method == 'GET':
        return render(request,'iniciarSession.html',{
                  'form': AuthenticationForm })
       else:
           user=authenticate(request, username=request.POST['username'],
                        password=request.POST['password'])
           if user is None:
               return render(request,'iniciarSession.html',{
                  'form': AuthenticationForm,
                   'error': 'el usuario o la contraseña son incorrectas'
                     })
           else:
               login(request, user)
               return redirect('principal')
#crud de pacientes
def pacientes(request):
    if request.method == 'GET':


     paci=pacientes1.objects.all()
     return render(request,'tabla_pacientes.html',{
        'pacien':paci,
        'form': busquedaP
        })
    else:
        form = busquedaP(request.POST)
        paci=pacientes1.objects.filter()

        return render(request,'tabla_pacientes.html',{
        'pacien':paci,
        'form': busquedaP
        })

def actualizar_paciente(request):
    paciente=get_object_or_404(pacientes1, pk=id)
    form = crear_paciente(instance = paciente)
    return render(request,'actualizar_paciente.html')

def crear_paciente(request):
    if request.method =='GET':

        return render(request,'crear_paciente.html',{

            'form':CreacionP
        })
    else:
        try:
            form=CreacionP(request.POST)
            new_paciente=form.save(commit=False)
            new_paciente.save()
            return redirect('pacientes')
        except ValueError:
            return render(request,'crear_paciente.html',{
                'form':CreacionP,
                'error':'verifique los datos'
            })

def mostrar_paciente(request,paciente_id):
    pacientes=get_object_or_404(pacientes1,pk=paciente_id)
    documents=documentos.objects.filter()
    return render(request,'mostrar_paciente.html',{
        'pacientes':pacientes,
        'documentos':documents
        })
def actualizar_paciente(request,paciente_id):
    if request.method=='GET':
        pacientes=get_object_or_404(pacientes1,pk=paciente_id)
        form=CreacionP(instance=pacientes)
        return render(request, "actualizar_paciente.html",{
            'pacientes':pacientes,
            'form':form
        } )
        return render
        

def agendas(request):
    return render(request,'agendas.html',)
#crud de documentos

def mostrar_documentos(request):
    return render(request,'documentos.html')

def crear_documentos(request):
    return render(request, 'documentos.html' )

