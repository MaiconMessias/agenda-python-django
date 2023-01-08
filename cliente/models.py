from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    datanascimento = models.DateTimeField('date nascimento')
    def __str__(self):
        return self.nome

class Contato(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    contato = models.CharField(max_length=200)
    def __str__(self):
        return self.contato