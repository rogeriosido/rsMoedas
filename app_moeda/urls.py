from django.urls import path
from .views import index, lista_moedas, novo_moedas, exclui_moedas, edita_moedas, lista_por_pais, lista_por_pais_tipo, lista_por_pais_tipo_ano

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('lista_moedas/', lista_moedas, name='lista_moedas'),
    path('novo_moedas/', novo_moedas, name='novo_moedas'),
    path('exclui_moedas/<int:id>/', exclui_moedas, name='exclui_moedas'),
    path('edita_moedas/<int:id>/', edita_moedas, name='edita_moedas'),    
    path('lista_por_pais/', lista_por_pais, name='lista_por_pais'),
    path('lista_por_pais_tipo/', lista_por_pais_tipo, name='lista_por_pais_tipo'),
    path('lista_por_pais_tipo_ano/', lista_por_pais_tipo_ano, name='lista_por_pais_tipo_ano'),
]