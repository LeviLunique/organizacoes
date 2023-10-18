from django.db import models

class Organizacao(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome
