from django.http import HttpResponse
import datetime
from django.template import Template, Context
class Persona(object):
    def __init__(self,nombre, apellido):

        self.nombre=nombre
        self.apellido=apellido    




def saludo(request):  # primra vista
    #nombre="juan"
    #apellido="Díaz"
    
    p1=Persona("Profesor Juan","Díaz")
    ahora=datetime.datetime.now()
    doc_externo=open("C:/Users/BenitezMartinE/OneDrive - VENG SA/GestionVENG/Cursos/django/proyecto1/proyecto1/plantillas/miplantilla.html") # abrir achivo
    plt=Template(doc_externo.read()) #Crear el objeto template
    doc_externo.close()  # Cerrar el archivo
    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora}) # Crear el contexto aunque esté vacio o un diccionario clave,nombre
    documento=plt.render(ctx) #redenrizar

    return HttpResponse(documento)


def despedida(request): #
    return HttpResponse("Hasta luego alumonos")


def dameFecha(request):
    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,edad,agno):
   #edadActual=18
    periodo=agno-2021
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(agno,edadFutura)
    return HttpResponse(documento)
