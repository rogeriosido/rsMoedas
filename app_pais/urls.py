from django.urls import path
from .views import lista_paises, novo_paises, exclui_paises, edita_paises

urlpatterns = [
    path('lista_paises/', lista_paises, name='lista_paises'),
    path('novo_paises/', novo_paises, name='novo_paises'),
    path('exclui_paises/<int:id>/', exclui_paises, name='exclui_paises'),
    path('edita_paises/<int:id>/', edita_paises, name='edita_paises'),    
]