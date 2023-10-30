from django.contrib import admin
from . models import Cargo, Chamado, Tipo, Setor, Situacao, Funcionario, Produto

# Register your models here.
admin.site.register(Chamado)
admin.site.register(Tipo)
admin.site.register(Setor)
admin.site.register(Situacao)
admin.site.register(Funcionario)
admin.site.register(Produto)
admin.site.register(Cargo)
