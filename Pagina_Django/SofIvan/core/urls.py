from django.urls import path 
from. views import index,inicio,somos,galeria,contacto,crear_usuario,reconocer,mod_usuario,ver_usuario,del_usuario,ver_contacto

urlpatterns = [

    
    path('',index,name="index"),
    path('inicio/', inicio, name="inicio"), 
    path('somos/', somos, name="somos"), 
    path('galeria/', galeria, name="galeria"), 
    path('contacto/', contacto, name="contacto"), 
    path('crear_usuario/', crear_usuario, name="crear_usuario"), 
    path('reconocer/', reconocer, name="reconocer"), 
    path('mod_usuario/<id>', mod_usuario, name="mod_usuario"), 
    path('ver_usuario/', ver_usuario, name="ver_usuario"), 
    path('ver_contacto/', ver_contacto, name="ver_contacto"), 
    path('del_usuario/<id>', del_usuario, name="del_usuario"),


]