from django.http import HttpResponse
 
def saludo(request):
  return HttpResponse("Hola mundo")

def segunda_vista(request):
  return HttpResponse("Segunda vista")