from django import forms
from .models import Moeda, Pais, Tipo

class MoedaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.valor is not None:
            self.initial['valor'] = "{:.2f}".format(self.instance.valor)
            
    class Meta:
        model = Moeda
        fields = ['pais','tipo','ano','valor','quantidade','quantidade_extra','quantidade_troca','quantidade_cunhagem','fao','observacoes','foto_frente','foto_verso','comemorativas',]

class MoedaFilterForm(forms.Form):
    pais = forms.ModelChoiceField(
        queryset=Pais.objects.all(),
        required=False,
        empty_label="Todos",
        widget=forms.Select(attrs={'id': 'pais-select', 'data-filter': 'pais'})
    )
    tipo = forms.ModelChoiceField(
        queryset=Tipo.objects.all(),
        required=False,
        empty_label="Todos",
        widget=forms.Select(attrs={'id': 'tipo-select', 'data-filter': 'tipo'})
    )