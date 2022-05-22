from django.contrib import admin
from django.urls import path
from Proyectocoder.views import saludo
from Proyectocoder.views import segunda_vista
urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/",saludo),
    path('segundavista/', segunda_vista)
]
