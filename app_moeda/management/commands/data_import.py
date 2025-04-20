import csv

from django.core.management.base import BaseCommand
from django.conf import settings

from app_moeda.models import Moeda, Pais, Tipo

class Command(BaseCommand):
    help = "Data import"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Arquivo CSV')

    def handle(self, *args, **kwargs):
        csv_file = open(f'{settings.BASE_DIR}/{kwargs["csv_file"]}')
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        for row in csv_reader:
            print(row)
            
            pais = Pais.objects.get(id=row['pais_id'])
            tipo = Tipo.objects.get(id=row['tipo_id'])

            moeda = Moeda(
                ano=row['ano'],
                valor=row['valor'],
                quantidade=row['quantidade'],
                quantidade_extra=row['quantidade_extra'],
                quantidade_troca=row['quantidade_troca'],
                quantidade_cunhagem=row['quantidade_cunhagem'],
                fao=row['fao'],
                foto_frente=row['foto_frente'],
                foto_verso=row['foto_verso'],                
                pais=pais,
                tipo=tipo,
                comemorativas=row['comemorativas']
            )
            moeda.save()