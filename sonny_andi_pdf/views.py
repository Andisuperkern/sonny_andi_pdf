from django.shortcuts import redirect, render
from django.http import HttpResponse
from .services import add


def prototype(request):
    return HttpResponse("Tagesziel erreicht! Zeit für Bier.")


def dummy_addition(request):
    a = 1
    b = 1
    return HttpResponse(f"Addition of a:{a} and b:{b} equals {add(a, b)}")


# /home
def home_view(request):
    return render(request, 'sonny_andi_pdf/home.html')
