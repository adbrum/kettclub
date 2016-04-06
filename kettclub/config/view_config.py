from django.contrib.auth.decorators import login_required, permission_required, \
    user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
# from kettclub.util.view_aux import pathLogotipo, statusIcon

@login_required
def configuracao(request):  
    # pathLogo = pathLogotipo()
    # listaInfo = statusIcon(request)
    
    template = "config/index.html"

    return render_to_response(template,
         locals(),
         context_instance = RequestContext(request)
         )


# editar Logotipo
@login_required    
def logo(request):
    return HttpResponseRedirect(reverse('config'))