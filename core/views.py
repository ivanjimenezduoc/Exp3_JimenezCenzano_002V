from django.shortcuts import render,redirect
from .models import Usuario,Contacto
from .forms import UsuarioForm,ContactoForm


# Create your views here.

def index(request):
    return render(request,'core/index.html')

def inicio(request):
    return render(request,'core/inicio.html')

def somos(request):
    return render(request,'core/somos.html')

def galeria(request):
    return render(request,'core/galeria.html')

def contacto(request):
    if request.method=='POST': 
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect('ver_contacto')
        else:
            contacto_form= ContactoForm()
    return render(request, 'core/contacto.html', {'contacto_form': ContactoForm})

def crear_usuario(request):
     if request.method=='POST': 
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('ver_usuario')
     else:
        usuario_form= UsuarioForm()
     return render(request, 'core/crear_usuario.html', {'usuario_form': UsuarioForm})

def reconocer(request):
    return render(request,'core/reconocer.html')

def ver_usuario(request):

    usuarios = Usuario.objects.all()
    print(usuarios)
    
    datos = {

        'usuarios':usuarios
     }
  
    return render(request, 'core/ver_usuario.html',datos)

def ver_contacto(request):

    contacto = Contacto.objects.all()
    
    datos = {

        'contactos':contacto
     }
  
    return render(request, 'core/ver_contacto.html',datos)


def mod_usuario(request,id):
  
    usuario = Usuario.objects.get(rut=id)
    datos = {
        'form': UsuarioForm(instance=usuario)
    }
    if request.method=='POST':
      
        formulario = UsuarioForm(data = request.POST, instance=usuario)
     
        if formulario.is_valid():
            print("deberia guardar")
            formulario.save()
            return redirect ('ver_usuario')
    return render (request, 'core/mod_usuario.html', datos )

def del_usuario(request, id):
    usuario = Usuario.objects.get(rut=id)
    usuario.delete()
    return redirect ('ver_usuario')