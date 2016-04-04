from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from kettclub.assiduousness.forms import AssiduityForm


# @cache_page(60)
from kettclub.assiduousness.models import Presenca
from kettclub.subscriptions.models import Subscription


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
    form = AssiduityForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'assiduity.html', locals())
    else:
        try:
            atleta = Subscription.objects.get(pk=pk_atleta)
        except Subscription.DoesNotExist as e:
            message = 'Nº de atleta não registado! Tente novamente.'

            return render(request, 'assiduity.html', locals())

        if atleta is not None:

            return render(request, 'assiduity.html', locals())


def success(request):
    form = AssiduityForm(request.POST or None)
    form.save()
    # return HttpResponseRedirect(r('subscriptions:'))
    return render(request, 'assiduity.html')
