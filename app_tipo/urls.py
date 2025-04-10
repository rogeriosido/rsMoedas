from django.urls import path
from .views import lista_tipos, novo_tipos, exclui_tipos, edita_tipos

urlpatterns = [
    path('lista_tipos/', lista_tipos, name='lista_tipos'),
    path('novo_tipos/', novo_tipos, name='novo_tipos'),
    path('exclui_tipos/<int:id>/', exclui_tipos, name='exclui_tipos'),
    path('edita_tipos/<int:id>/', edita_tipos, name='edita_tipos'),
]