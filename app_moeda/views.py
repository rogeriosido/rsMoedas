from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Count

from .models import Moeda, Pais, Tipo
from .forms import MoedaForm, MoedaFilterForm

@login_required
def index(request):
    form = MoedaFilterForm(request.GET)
    moedas = Moeda.objects.none()

    if request.method == 'GET' and form.is_valid():
        pais = form.cleaned_data.get('pais')
        tipo = form.cleaned_data.get('tipo')

        if pais or tipo:
            moedas = Moeda.objects.all()
            if pais:
                moedas = moedas.filter(pais=pais)
            if tipo:
                moedas = moedas.filter(tipo=tipo)

    context = {
        'form': form,
        'moedas': moedas,
    }
    return render(request, 'index.html', context)

@login_required
def lista_moedas(request):
    form = MoedaFilterForm(request.GET)
    moedas = Moeda.objects.none()

    if request.method == 'GET' and form.is_valid():
        pais = form.cleaned_data.get('pais')
        tipo = form.cleaned_data.get('tipo')

        if pais or tipo:
            moedas = Moeda.objects.all()
            if pais:
                moedas = moedas.filter(pais=pais)
            if tipo:
                moedas = moedas.filter(tipo=tipo)

        moedas = moedas.order_by('pais','tipo','ano','valor') # Ordena os resultados

    context = {
        'form': form,
        'moedas': moedas,
    }
    return render(request, 'lista_moedas.html', context)

@login_required
def novo_moedas(request):
    if request.method == 'POST':
        form = MoedaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            aviso = 'Moeda salva com sucesso'
            messages.success(request,aviso)            
            return redirect('index')
    else:
        form = MoedaForm()
    return render(request, 'cadastro_moeda.html', {'form': form})

@login_required
def edita_moedas(request, id):
    moeda = get_object_or_404(Moeda, id=id)
    try:
        if request.method == 'POST':
            form = MoedaForm(request.POST, request.FILES, instance=moeda)
            if form.is_valid():
                form.save()
                aviso = 'Moeda salva com sucesso'
                messages.success(request, aviso)
                return redirect('index')
        else:
            form = MoedaForm(instance=moeda)
        return render(request, 'cadastro_moeda.html', {'form': form, 'moeda': moeda})
    except Exception as e:
        messages.error(request, f"Ocorreu um erro: {e}")
        return render(request, 'cadastro_moeda.html', {'form': form, 'moeda': moeda})

@login_required
def exclui_moedas(request, id):
    moeda = get_object_or_404(Moeda, id=id)
    moeda.delete()
    aviso = 'Moeda apagada com sucesso'
    messages.success(request,aviso)            
    return redirect('index')

@login_required
def lista_por_pais(request):
    total_por_pais = Moeda.objects.values('pais__nome').annotate(totalpais=Count('id')).order_by('pais__nome')
    total_com_quantidade = Moeda.objects.filter(quantidade__gt=0).values('pais__nome').annotate(totalquantidade=Count('id')).order_by('pais__nome')
    total_sem_quantidade = Moeda.objects.filter(quantidade=0).values('pais__nome').annotate(totalsemquantidade=Count('id')).order_by('pais__nome')

    # Criar um dicionário para combinar os resultados
    resultados = {}
    for item in total_por_pais:
        resultados[item['pais__nome']] = {'totalpais': item['totalpais'], 'totalquantidade': 0, 'totalsemquantidade': 0}

    for item in total_com_quantidade:
        if item['pais__nome'] in resultados:
            resultados[item['pais__nome']]['totalquantidade'] = item['totalquantidade']
        else:
            resultados[item['pais__nome']] = {'totalpais': 0, 'totalquantidade': item['totalquantidade'], 'totalsemquantidade': 0}

    for item in total_sem_quantidade:
        if item['pais__nome'] in resultados:
            resultados[item['pais__nome']]['totalsemquantidade'] = item['totalsemquantidade']
        else:
            resultados[item['pais__nome']] = {'totalpais': 0, 'totalquantidade': 0, 'totalsemquantidade': item['totalsemquantidade']}

    # Converter o dicionário em uma lista de dicionários para o template
    lista_resultados = [{'pais__nome': pais, 'totalpais': dados['totalpais'], 'totalquantidade': dados['totalquantidade'], 'totalsemquantidade': dados['totalsemquantidade']} for pais, dados in resultados.items()]

    return render(request, 'lista_por_pais.html', {'lista_resultados': lista_resultados})

@login_required
def lista_por_pais_tipo(request):
    pais_nome = request.GET.get('pais')

    moedas = Moeda.objects.all()

    if pais_nome:
        try:
            pais = Pais.objects.get(nome=pais_nome)
            moedas = moedas.filter(pais=pais)
        except Pais.DoesNotExist:
            moedas = Moeda.objects.none()  # Nenhum país encontrado, retorna lista vazia

    resultados = moedas.values('pais__nome', 'tipo__nome').annotate(quantidade=Count('id')).order_by('tipo__nome')

    paises = Pais.objects.all()

    context = {
        'resultados': resultados,
        'paises': paises,
        'pais_selecionado': pais_nome,
    }
    return render(request, 'lista_por_pais_tipo.html', context)

@login_required
def lista_por_pais_tipo_ano(request):
    pais_nome = request.GET.get('pais')
    tipo_nome = request.GET.get('tipo')

    moedas = Moeda.objects.all()

    if pais_nome and tipo_nome:
        try:
            pais = Pais.objects.get(nome=pais_nome)
            tipo = Tipo.objects.get(nome=tipo_nome)
            moedas = moedas.filter(pais=pais, tipo=tipo)
        except (Pais.DoesNotExist, Tipo.DoesNotExist):
            moedas = Moeda.objects.none()

    resultados = moedas.values('ano').annotate(quantidade=Count('id')).order_by('ano')

    context = {
        'resultados': resultados,
        'pais_selecionado': pais_nome,
        'pais_id': pais.id,
        'tipo_selecionado': tipo_nome,
        'tipo_id': tipo.id,
    }
    return render(request, 'lista_por_pais_tipo_ano.html', context)