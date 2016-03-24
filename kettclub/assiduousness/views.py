from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from kettclub.assiduousness.forms import AssiduityForm
from kettclub.core.models import Presenca


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
    return render(request, 'assiduousness/assiduity_form.html',
                  {'form': AssiduityForm()})
