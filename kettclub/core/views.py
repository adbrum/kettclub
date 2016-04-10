from django.shortcuts import render
from django.views.generic import TemplateView
from kettclub.administration.forms import LoginForm


class home(TemplateView):
    template_name ='home.html'


# def home(request):
#     return render(request, 'home.html', {'form': LoginForm})

# class success(TemplateView):
#     template_name = 'success.html'


# def success(request):
#     return render(request, 'success.html')


class unauthorized(TemplateView):
    template_name = 'pagina_nao_autorizada.html'

# def unauthorized(request):
#     return render(request, 'pagina_nao_autorizada.html')
