from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pessoa(models.Model):
    nome=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    cpf=models.int(max_length=11)
    usuario=models.ForeignKey(User,null=True, blank=False )
    def __str__(self):
        return self.nome
class Evento(models.Model):
    nome=models.CharField(max_length=100)
    dataInicio=models.DateTimeField()
    dataFinal=models.DateTimeField()
    local=models.CharField(max_length=100)

class Ticket(models.Model):
    nome=models.CharField(max_length=128)
    descricao=models.CharField(max_length=128)
    valor=models.money(max_length=128)
    evento=models.ForeignKey(Evento, null=True, blank=False)

class Inscricao(models.Model):
    validação=models.BooleanField(default=False)
    evento=models.ForeignKey(Evento, null=True, blank=False)
    pessoa=models.ForeignKey(Pessoa, null=True, blank=False)
    ticket=models.ForeignKey(Ticket, null=True, blank=False)