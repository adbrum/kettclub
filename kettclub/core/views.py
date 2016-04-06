from django.shortcuts import render
from kettclub.administration.forms import LoginForm


def home(request):
    return render(request, 'home.html', {'form': LoginForm})


def success(request):
    return render(request, 'success.html')


def unauthorized(request):
    return render(request, 'pagina_nao_autorizada.html')