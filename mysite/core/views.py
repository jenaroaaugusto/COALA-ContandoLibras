from django.shortcuts import render

from core.forms import SubscriptionForm
from django.http import HttpResponse


def home(request):
    return render(request, 'core/index.html')


def contato(request):
    form = SubscriptionForm()
    return render(request, 'core/contato.html', {'form': form})


def contos(request):
    return render(request, 'core/contos.html')


def jogos(request):
    return render(request, 'core/jogos.html')


def memoria(request):
    return render(request, 'core/memoria.html')


def desenhos(request):
    return render(request, 'core/desenhos.html')
