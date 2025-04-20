from django import forms
from .models import Pais

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nome']
