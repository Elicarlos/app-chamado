from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Base(models.Model):
    create_at = models.DateTimeField(default=timezone.now, editable=True)
    update_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        super().save(*args, **kwargs)


class Cargo(Base):
    descricao = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.descricao

class Setor(Base):
    setor = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.setor
    


class Funcionario(User):
    nome = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, related_name='funcionarios_cargo')
    setor = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, related_name='funcionarios_setor')

    def __str__(self):
        return self.nome

    

# Create your models here.
# Garantia / Contrato / Externo / Solicitação Peça
class Tipo(Base):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao



# Concluido / Em Execução / Verificao / Aguardando Peça
class Situacao(Base):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao




class Produto(Base):
    codigo_barras = models.CharField(max_length=20, unique=True)
    codigo = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.FloatField()

    def __str__(self):
        return self.descricao
 


class Chamado(Base):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)
    ordem_servico = models.CharField(max_length=100)  # Referente ao shop9
    situacao = models.ForeignKey(Situacao, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=100)    
    setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True)
    produtos = models.ManyToManyField(Produto, blank=True)
    data_abertura = models.DateField()
    data_aprovacao = models.DateField(null=True, blank=True)
    aberta_por = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, related_name='chamados_abertos', null=True, blank=True)
    aprovada_por = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, related_name='chamados_aprovados', null=True, blank=True)
    fechada_por = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, related_name='chamados_fechados', null=True, blank=True)
    data_fechamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

