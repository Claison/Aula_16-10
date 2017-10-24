from rest_framework import  serializers, viewsets
from django.contrib.auth.models import User
from evento.models import Pessoa,Evento,Ticket,Inscricao
#ViewsSets define the view dehavior.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('username','email','is_staff')

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    usuario=UserSerializer(many=False)
    class Meta:
        model=Pessoa
        fields=('nome','email','cpf','usuario')
        #read_only_fields=('cpf',)

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    dataInicio=serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    dataFinal=serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    class Meta:
        model=Evento
        fields=('nome','dataInicio','dataFinal','local')

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    evento=EventoSerializer(many=False)
    class Meta:
        model=Ticket
        fields=('nome','descricao','valor','evento')

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    evento=EventoSerializer(many=False)
    pessoa=PessoaSerializer(many=False)
    ticket=TicketSerializer(many=False)
    class Meta:
        model=Inscricao
        fields=('validacao','evento','pessoa','ticket')


