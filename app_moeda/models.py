from django.db import models
from django.core.validators import MinValueValidator

from app_pais.models import Pais
from app_tipo.models import Tipo

class Moeda(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    ano = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    quantidade = models.IntegerField(default=0)
    quantidade_extra = models.IntegerField(default=0)
    quantidade_troca = models.IntegerField(default=0)
    quantidade_cunhagem = models.IntegerField(default=0)
    fao = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True, null=True)
    foto_frente = models.FileField(upload_to='moedas', default=None, null=True, blank=True)
    foto_verso = models.FileField(upload_to='moedas', default=None, null=True, blank=True)
    comemorativas = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"{self.tipo} - {self.pais} ({self.ano})"