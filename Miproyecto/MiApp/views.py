from django.shortcuts import render

from MiApp.models import Familiares

# Create your views here.
def mostrar_familiares(request):

    fam1 = Familiares(nombre="Fernando", apellido="Gasperi", edad= 32, cumple="1990-07-10")
    fam2 = Familiares(nombre="Maria", apellido="Gasperi", edad= 31, cumple="1991-01-05")
    fam3 = Familiares(nombre="Pedro", apellido="Gasperi", edad= 22, cumple="2000-04-15")

    return render(request, "MiApp/familiares.html", {"Familiares":[fam1,fam2,fam3]})