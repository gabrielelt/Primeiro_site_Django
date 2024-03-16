from django.db import models
from django.contrib.auth.models import AbstractUser

class Aluno_Profile( AbstractUser):

    def __str__(self):
        return self.username
