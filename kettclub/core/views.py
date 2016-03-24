from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from kettclub.administration.forms import LoginForm


@cache_page(60)
def home(request):
    context = {'form': LoginForm}
    return render(request, 'home.html', context, context_instance=RequestContext(request))
