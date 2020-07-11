from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.http import require_http_methods
from .models import Conductor, Viaje
from .forms import ViajeForm

# Create your views here.


def home(request):
    return render(request, "base-login.html", {})

def login(request):
    return render(request, "forms/signIn.html", {})

@require_http_methods(["GET", "POST"])
def EmpezarViaje(request):
    if request.method == "POST":
        form = ViajeForm(request.POST)
        if form.is_valid():
            form.save()
            #asistencia = Asistencia.objects.get(pk=id)
            #asistencia.asistencia = 'Justificada'
            #asistencia.save()
            return 0
    else:
        form = ViajeForm
        return render(request, "viajes/empezar.html", {"form": form})

