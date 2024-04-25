"""SistemaConvenios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin  # pragma: no cover
from django.urls import path, include  # pragma: no cover
from convenios.views import Bienvenida, mostrar_diversas_instituciones, \
      mostar_internacionales, mostrar_nacionales, mostar_pendientes, mostar_varios, agregar_convenio, \
      borrar_convenio, editar_convenio, mostar_detalles_convenio, agregar_unidad_academica, agregar_persona  # pragma: no cover
from django.conf import settings  # pragma: no cover
from django.conf.urls.static import static  # pragma: no cover

urlpatterns = [  # pragma: no cover
    path('admin/', admin.site.urls),
    path('', Bienvenida.as_view(), name='bienvenida'),
    path('diversas_instituciones/', mostrar_diversas_instituciones,
         name="diversas_instituciones"),
    path('internacionales/', mostar_internacionales, name="internacionales"),
    path('nacionales/', mostrar_nacionales, name="nacionales"),
    path('pendientes/', mostar_pendientes, name="pendientes"),
    path('varios/', mostar_varios, name="varios"),
    path('usuarios/', include('usuarios.urls')),
    path('agregar_convenio/', agregar_convenio, name="agregar_convenio"),
    path('borrar_convenio/<int:convenio_id>',
         borrar_convenio, name="borrar_convenio"),
    path('editar_convenio/<int:convenio_id>',
         editar_convenio, name="editar_convenio"),
    path('agregar_unidad/', agregar_unidad_academica, name="agregar_unidad"),
    path('agregar_persona/', agregar_persona, name="agregar_persona"),
    path('mostrar_detalles_convenio/<int:convenio_id>',
         mostar_detalles_convenio, name="mostar_detalles_convenio"),

]

if settings.DEBUG:  # pragma: no cover
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
