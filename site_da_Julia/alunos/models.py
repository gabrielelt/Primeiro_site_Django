from django.db import models
from django.contrib.auth.models import AbstractUser

class Aluno_Profile(AbstractUser):
    matricula = models.CharField(max_length=10, unique=True)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.username
