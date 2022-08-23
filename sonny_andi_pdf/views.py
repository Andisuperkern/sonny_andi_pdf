from django.shortcuts import redirect, render
from django.http import HttpResponse


def prototype(request):
    return HttpResponse("Hello World")
