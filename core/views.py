from django.shortcuts import redirect, render
from django.http import HttpResponse
from . forms import ChamadoForm
from . models import Tipo, Setor, Situacao

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/index.html')
@login_required
def dasboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def cadastro_funcionario(request):
    return render(request, 'core/cad-funcionario.html')

@login_required
def cadastro_produto(request):
    return render(request, 'core/cad-produto.html')

@login_required
def lista_funcionario(request):
    return render(request, 'core/list-funcionarios.html')

@login_required
def chamados(request):
    if request.method == "POST":
        form = ChamadoForm(request.POST)
        print(form)
        if form.is_valid():
            novo_chamado = form.save(commit=False)
            novo_chamado.usuario = request.user
            novo_chamado.save()
            return redirect('Salvo com sucesso')
        
        else:
            erros = form.errors
                # Além disso, você pode acessar os campos que deram erro individualmente.
            campo_tipo = form['tipo']
            campo_setor = form['setor']
            
    else:
        form = ChamadoForm()

    tipos = Tipo.objects.all()
    setores = Setor.objects.all()
    situacoes = Situacao.objects.all()

    return render(request, 'core/chamado.html', {
        'form': form, 
        'tipos': tipos,
        'setores': setores,
        'situacoes': situacoes
        })

def graficos(request):
    pass

