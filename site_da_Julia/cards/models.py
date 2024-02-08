from django.db import models
from django.core.exceptions import ValidationError

class Card(models.Model):
    CLASSES_CARDS = [
        ('', 'Selecione a classe do card'),
        ('Frutas', 'Frutas'),
        ('Animais', 'Animais'),
        ('Objetos', 'Objetos'),
        ('Pessoas', 'Pessoas'),
        ('Veículos', 'Veículos'), 
    ]

    nome_do_card = models.CharField(max_length=100, null=False, blank=False)
    classe_do_card = models.CharField(max_length=100, default='', choices = CLASSES_CARDS)
    publicada = models.BooleanField(default=False)
    alternativa_um = models.CharField(max_length=100, null=False, blank=False)
    alternativa_dois = models.CharField(max_length=100, null=False, blank=False)
    alternativa_tres = models.CharField(max_length=100, null=False, blank=False)
    alternativa_quatro = models.CharField(max_length=100, null=False, blank=False)
    alternativa_cinco = models.CharField(max_length=100, null=False, blank=False)

    resposta_correta = models.CharField(max_length=100, null= False, blank=False)
 
    foto_card = models.ImageField(upload_to='cards_fotos/%Y/%m/%d/', null=True, blank=True)
    
    def __str__(self):
        return self.nome_do_card