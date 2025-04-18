from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

from .models import Pais
from .forms import PaisForm

@login_required
def lista_paises(request):
    paises = Pais.objects.all()
    return render(request, 'lista_paises.html',{'paises': paises})

@login_required
def novo_paises(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'Pais salvo com sucesso'
            messages.success(request,aviso)            
            return redirect('index')
    else:
        form = PaisForm()
    return render(request, 'cadastro_pais.html', {'form': form})

@login_required
def edita_paises(request, id):
    pais = get_object_or_404(Pais, id=id)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=pais)
        if form.is_valid():
            form.save()
            aviso = 'Pais salvo com sucesso'
            messages.success(request,aviso)            
            return redirect('index')
    else:
        form = PaisForm(instance=pais) 
    return render(request, 'cadastro_pais.html', {'form': form, 'pais': pais})

@login_required
def exclui_paises(request, id):
    pais = get_object_or_404(Pais, id=id)
    pais.delete()
    aviso = 'Pais apagado com sucesso'
    messages.success(request,aviso)            
    return redirect('index')
