from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Habitant(object):

    def __init__(self, nombre, apellido, agnoNacimiento, ciudad):

        self.nombre = nombre
        self.apellido = apellido
        self.agnoNacimiento = agnoNacimiento
        self.ciudad = ciudad

def saludo(request):

    Alumne=Habitant("Adrián", "Sánchez", 2003, "Badalona")

    ahora=datetime.datetime.now()

    modu=["programacio web","des. servidor","desplegament apps web","disseny interficies","projecte"]

    doc_externo = open("C:/Users/Administrator/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nom":Alumne.nombre, "cognom":Alumne.apellido, "any":Alumne.agnoNacimiento, "ciutat":Alumne.ciudad, "moment_actual": ahora, "modulos": modu})

    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego alumnos de Django")

def ruta(request):

    return HttpResponse("Esta es la tercera ruta")

def dameFecha(request):

    fecha_actual=datetime.datetime.today()
    diferencia_agno=datetime.datetime(fecha_actual.year, 12, 31)
    diferencia=(diferencia_agno - fecha_actual).days

    documento="""<html>
    <body>
    <table style="border: 1px solid black;">
    <tr>
    <th>
    Fecha y hora actuales
    </th>
    <th>
    Hasta final de año queda
    </th>
    </tr>
    <tr>
    <td style="border: 1px solid black;">
    %s
    </td>
    <td style="border: 1px solid black;">
    %s
    </td>
    </tr>
    </table>
    </body>
    </html>""" % (fecha_actual, diferencia)

    return HttpResponse(documento)

def nombreAgno(request, nombre, agno):

    nAgnos= datetime.date.today().year - agno

    documento="""<html>
    <body>
    <h1>
    %s nació en %s y tiene %s años
    </h1>
    </body>
    </html>""" % (nombre, agno, nAgnos)

    return HttpResponse(documento)