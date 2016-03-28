from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import resolve_url as r
from django.views.decorators.cache import cache_page
from kettclub.assiduousness.forms import AssiduityForm
from kettclub.core.models import Presenca, Atleta


@cache_page(60)
@login_required
def listassiduity(request):
    now = datetime.now()

    dmin = request.POST.get('date1')
    dmax = request.POST.get('date2')

    if dmax == None:
        min_date = now.strftime("%Y-%m-%d")
        max_date = now.strftime("%Y-%m-%d")
    else:
        min_date = datetime.strptime(dmin, "%d/%m/%Y")
        max_date = datetime.strptime(dmax, "%d/%m/%Y")

    list_assiduity = Presenca.objects.filter(datapresenca__gte=min_date, datapresenca__lte=max_date).order_by(
        '-datapresenca')

    context = {
        'list': list_assiduity
    }
    # tamLista = len(list_inscription)

    return render(request, "assiduousness/index.html", context)


# @cache_page(60)
def new(request):
    pk_atleta = request.POST.get('numeroatleta')
    data = request.POST.get('datapresenca')
    print('pk_atleta', pk_atleta)
    form = AssiduityForm(request.POST or None)
    if not form.is_valid():
        print('FORM NÂO', request.GET)
        return render(request, 'assiduity.html', locals())
    else:
        print('FORM SIM', request.POST)
        atleta = Atleta.objects.get(pk=pk_atleta)
        if atleta is not None:
            print('ATLETA SIM', request.POST)
            # form.save()
            return render(request, 'assiduity.html', locals())

        message = 'Nº de atetla inisistente!'
        return render(request, 'assiduity.html', locals())


def success(request):
    print('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
    form = AssiduityForm(request.POST or None)
    form.save()
    # return HttpResponseRedirect(r('subscriptions:'))
    return render(request, 'assiduity.html')