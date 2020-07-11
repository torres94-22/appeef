from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Conductor, Viaje
from django.contrib.auth.models import User
from .forms import ViajeForm, AceptarForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

# Create your views here.


def home(request):
    return render(request, "base-login.html", {})

def listadoViajesU(request):
    viajes = Viaje.objects.filter(viajero=request.user)
    return render(request, "viajes/listado.html", {'viajes': viajes})

def login(request):
    return render(request, "forms/signIn.html", {})

def listar_viajes(request, id=1):
    viajes = Viaje.objects.filter(viajero=request.user)
    return render(
        request,
        "viajes/lista-viajes.html",
        { "viajes": viajes },
    )

@require_http_methods(["GET", "POST"])
def EmpezarViaje(request):
    if request.method == "POST":
        form = ViajeForm(request.POST)
        if form.is_valid():
            viaje = Viaje(viajero=request.user,distrito=form.cleaned_data['distrito'],destino=form.cleaned_data['destino'])
            viaje.save()
            return redirect('appeff:index')
    else:
        form = ViajeForm
        return render(request, "viajes/empezar.html", {"form": form})

@require_http_methods(["GET", "POST"])
def AceptarViaje(request,id=1):
    form = AceptarForm(request.POST)
    if form.is_valid():
        viaje = Viaje.objects.get(pk=id)
        viaje.conductor = Conductor.objects.get(pk=request.user.id)
        viaje.status="1"
        viaje.precio=form.cleaned_data['precio']
        viaje.save()
        conductor = Conductor.objects.get(pk=viaje.conductor.id)
        conductor.disponibilidad = 1
        conductor.save()
        return redirect('appeff:index')
    else:
        form = AceptarForm
        return render(request, "viajes/aceptar-viaje.html", {"form": form})

    

def CulminarViaje(request,id=1):
    viaje = Viaje.objects.get(pk=id)
    viaje.status=1
    print(viaje_conductor_disponibilidad)
    viaje.save()
    return redirect('appeff:index')
