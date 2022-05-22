from django.http import HttpResponse
import datetime
def saludo(request):
  return HttpResponse("Hola mundo")

def segunda_vista(request):
  return HttpResponse("Segunda vista")

def DiaDeHoy(request):
  dia = datetime.datetime.now()
  texto = "hoy es:{}".format(dia)
  return HttpResponse(texto)

def nombre_persona(self, nombre):
  resultado = "Mi nombre es:<br> <br> {}".format(nombre)
  return HttpResponse(resultado)