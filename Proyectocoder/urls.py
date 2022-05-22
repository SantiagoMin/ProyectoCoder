from django.contrib import admin
from django.urls import path
from Proyectocoder.views import saludo
from Proyectocoder.views import segunda_vista
from Proyectocoder.views import DiaDeHoy
from Proyectocoder.views import nombre_persona
urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/",saludo),
    path('segundavista/', segunda_vista),
    path("diaDeHoy/", DiaDeHoy),
    path("nombre_persona/<nombre>/",nombre_persona)
]
