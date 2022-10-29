from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html", {
    })


def multiplicar(request):
    val1 = int(request.POST.get("val1"))
    val2 = int(request.POST.get("val2"))
    mul = val1 * val2
    resultado = "La multiplicación de {} y {} es: {}".format(val1, val2, mul)
    return render(request, "index.html", { 
        "resultado": resultado
    })

def sumar(request):
    val1 = int(request.POST.get("val1"))
    val2 = int(request.POST.get("val2"))
    sum = val1 + val2
    resultado = "La suma de {} y {} es: {}".format(val1, val2, sum)
    return render(request, "index.html", { 
        "resultado": resultado
    })





def resta(request):
    val1 = int(request.POST.get("val1"))
    val2 = int(request.POST.get("val2"))
    res = val1 - val2
    resultado = "La resta de {} y {} es : {}".format(val1, val2, res)
    return render(request, "index.html", { 
        "resultado": resultado
    })



   
def dividir(request):
    val1 = int(request.POST.get("val1"))
    val2 = int(request.POST.get("val2"))
    div = val1 // val2
    saludo = "Hola Tripulantes"
    resultado = "La división de {} y {} es: {}".format(val1, val2, div) 
    return render(request, "index.html", { 
        "resultado": resultado,
        "saludo" : saludo
    })

    
def potencia(resquest, val1, val2):
    val1 = int(val1)
    val2 = int(val2)
    pot = val1 ** val2 
    resultado = "El número {} elevado a la {} es: {}".format(val1, val2, pot) 
    return render(request, "index.html", { 
        "resultado": resultado
    })

