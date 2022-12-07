from django.shortcuts import render, redirect
from .models import Disco

# Create your views here.
def home(request):
    discos = Disco.objects.all()
    return render(request, 'discos.html', {'discos': discos})

def crear_disco(request):
    disco = Disco(nombre=request.POST['nombre'], 
                  autor=request.POST['autor'], 
                  estilo=request.POST['estilo'], 
                  )
    disco.save()
    return redirect('/')

def borrar_disco(request, disco_id):
    disco = Disco.objects.get(id=disco_id)
    disco.delete()
    return redirect('/')

def editar_disco(request, disco_id):
    disco = Disco.objects.get(id=disco_id)
    disco.delete()
    return render(request, 'form.html', {'disco' : disco})
    