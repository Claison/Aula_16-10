from django.contrib import admin
from evento.models import Pessoa,Evento,Ticket,Inscricao
# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Evento)
admin.site.register(Ticket)
admin.site.register(Inscricao)