from django.db import models
from django.core.exceptions import ValidationError
from alunos.models import Aluno_Profile

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
    aluno = models.ManyToManyField(Aluno_Profile, related_name="cards_respondidos" , through='Aluno_Card')

    def __str__(self):
        return self.nome_do_card

class Aluno_Card(models.Model):
    aluno = models.ForeignKey(Aluno_Profile, on_delete=models.CASCADE, related_name='aluno_card')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='aluno_card')
    acertou = models.BooleanField(null=False, blank=False)
    data_acerto = models.DateTimeField(auto_now_add=True)
    data_erro = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.acertou:
            if self.data_acerto is None:
                raise ValidationError('Data de acerto não pode ser nula')
            if self.data_erro is not None:
                raise ValidationError('Data de erro deve ser nula')
        else:
            if self.data_erro is None:
                raise ValidationError('Data de erro não pode ser nula')
            if self.data_acerto is not None:
                raise ValidationError('Data de acerto deve ser nula')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Aluno: {self.aluno} - Card: {self.card} - Acertou: {self.acertou} - Data de acerto: {self.data_acerto} - Data de erro: {self.data_erro}'

    class Meta:
        unique_together = ['aluno', 'card']
        verbose_name = 'Aluno_Card'
        verbose_name_plural = 'Alunos_Cards'