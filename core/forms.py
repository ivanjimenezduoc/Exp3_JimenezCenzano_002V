from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import  Usuario,Contacto


class UsuarioForm(forms.ModelForm):

    class Meta: 
        model= Usuario
        fields = ['rut', 'nombre', 'apellido', 'telefono', 'correo','password']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'apellido': 'Apellido ', 
            'telefono': 'Telefono', 
            'correo': 'Correo',
            'password':'Contraseña'
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombres', 
                    'id': 'nombre'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Apellidos', 
                    'id': 'apellido'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Telefono', 
                    'id': 'telefono'
                }
            ), 
             'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo', 
                    'id': 'correo'
                }
                ),
              'password': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'type':'password',
                    'placeholder': 'Ingrese Contraseña', 
                    'id': 'password'
                }
                )
                
            
            

        }


class ContactoForm(forms.ModelForm):
    class Meta: 
        model= Contacto
        fields = ['rut', 'nombre', 'apellido', 'telefono', 'correo','comentario']
        labels ={

            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'apellido': 'Apellido ', 
            'telefono': 'Telefono', 
            'correo': 'Correo',
            'comentario':'Comentarios'
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombres', 
                    'id': 'nombre'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Apellidos', 
                    'id': 'apellido'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Telefono', 
                    'id': 'telefono'
                }
            ), 
             'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo', 
                    'id': 'correo'
                }
                ),
              'comentario': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese sus comentarios',
                    'rows':5, 
                    'id': 'comentario'
                }
                )
                
            
            

        }