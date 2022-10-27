from cgitb import reset
from datetime import timezone
from email import message
from re import A
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from reservasAPP.models import reserva
from reservasAPP.forms import FormProyecto
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def listadoreservas(request):
    reservas = reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if  form.is_valid():
            form.save()
        return index(request) 

    data = {'form' : form}
    return render(request, 'agregarReserva.html', data)

def eliminarReserva(request, id):
    Res = reserva.objects.get(id= id)
    Res.delete()
    return redirect('/reservas')

def actualizarReserva(request, id):
    Res= reserva.objects.get(id = id)
    form=FormProyecto(instance=Res)
    if request.method=='POST':
        form=FormProyecto(request.POST, instance=Res)
        if form.is_valid():
            form.save()
        return index (request)
    data ={'form':form}
    return render (request, 'agregarReserva.html',data)

