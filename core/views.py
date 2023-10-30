from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def dasboard(request):
    return render(request, 'core/dashboard')


def cadastro(request):
    return render('core/cadatro.html')


def chamados(request):
    pass

def graficos(request):
    pass

