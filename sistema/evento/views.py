from django.shortcuts import render
from .models import Pessoa,Evento,Ticket,Inscricao
from rest_framework import viewsets
from django.contrib.auth.models import User
from evento.serializers import UserSerializer,PessoaSerializer,EventoSerializer,TicketSerializer,InscricaoSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset=Pessoa.objects.all()
    serializer_class=PessoaSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset=Evento.objects.all()
    serializer_class=EventoSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset=Ticket.objects.all()
    serializer_class=TicketSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset=Inscricao.objects.all()
    serializer_class=InscricaoSerializer