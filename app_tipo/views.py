from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

from .models import Tipo
from .forms import TipoForm

@login_required
def lista_tipos(request):
    tipos = Tipo.objects.all()
    return render(request, 'lista_tipos.html',{'tipos': tipos})

@login_required
def novo_tipos(request):
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'Tipo salvo com sucesso'
            messages.success(request,aviso)            
            return redirect('index')
    else:
        form = TipoForm()
    return render(request, 'cadastro_tipo.html', {'form': form})

@login_required
def edita_tipos(request, id):
    tipo = get_object_or_404(Tipo, id=id)
    if request.method == 'POST':
        form = TipoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            aviso = 'Tipo salvo com sucesso'
            messages.success(request,aviso)            
            return redirect('index')
    else:
        form = TipoForm(instance=tipo) 
    return render(request, 'cadastro_tipo.html', {'form': form, 'tipo': tipo})

@login_required
def exclui_tipos(request, id):
    tipo = get_object_or_404(Tipo, id=id)
    tipo.delete()
    aviso = 'Tipo apagado com sucesso'
    messages.success(request,aviso)            
    return redirect('index')
