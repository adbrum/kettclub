from django.shortcuts import render
from kettclub.administration.forms import LoginForm


def home(request):
    return render(request, 'home.html', {'form': LoginForm})
