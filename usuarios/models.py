from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Usuário'

    def __str__(self):
        return self.nome