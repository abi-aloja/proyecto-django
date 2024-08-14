"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros
#permite acceder a variabkes MEDIA_URL y MEDIA_ROOT que almacenan la ubicación de nuestras imagenes.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="principal"),
    path('contacto/',views_registros.contacto, name="contacto"),
    path('formulario/',views.formulario,name="formulario"),
    path('seguridad/', views.seguridad, name="Segurdidad"),
    path('registrar/',views_registros.registrar, name="registrar"),
    path('comentario/',views_registros.regcontacto, name="comentario"),
    path('eliminarComentario/<int:id>',views_registros.eliminarComentarioContacto, name='Eliminar'),
    path('formEditarComentario/<int:id>/', views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name='Editar'),
    path('consultas1', views_registros.consultar1,name="Consultas"),
    path('consultas2', views_registros.consultar2,name="Consultas"),
    path('consultas3', views_registros.consultar3,name="Consultas"),
    path('consultas4', views_registros.consultar4,name="Consultas"),
    path('consultas5', views_registros.consultar5,name="Consultas"),
    path('consultas6', views_registros.consultar6,name="Consultas"),
    path('consultas7', views_registros.consultar7,name="Consultas"),
    path('consultasSQL', views_registros.consultasSQL,name="consultasSQL"),
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

   