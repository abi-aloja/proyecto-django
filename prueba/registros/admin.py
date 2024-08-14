from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Alumnos 
from .models import Comentario
from .models import ComentarioContacto
# Register your models here.

class AdministrarComentarios(admin.ModelAdmin):
    list_display=('id','coment')
    search_fields=('id','created')
    date_hierarchy ='created'
    list_filter =('created','id')

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display=('id','mensaje')
    search_fields=('id','created')
    date_hierarchy ='created'
    list_filter =('created','id')

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera','turno', 'created')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')
    list_per_page= 2
    list_display_links=('matricula','nombre')
    list_editable=('turno',)

    def get_readonly_fields(self, request, obj=None):
        #si el usuario pertenece al grupo de permisos "Usuarios"
        if request.user.groups.filter(name="Usuarios").exists():
            #bloquea los campos
            return ( 'matricula', 'carrera', 'turno')
        #cualquier otro usuario que no pertenece al grupo "Usuario"
        else: 
            #bloaquera los campos
            return('created', 'updated')
            
admin.site.register(Alumnos, AdministrarModelo)
admin.site.register(Comentario, AdministrarComentarios)
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
