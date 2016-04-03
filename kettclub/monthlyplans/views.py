from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import resolve_url as r
from django.views.decorators.cache import cache_page

from kettclub.monthlyplans.forms import MonthlyPlansForm


# @cache_page(60)
from kettclub.monthlyplans.models import PlanoMensalidade


@login_required
def listmonthlyplan(request, *args, **kwargs):
    list_plans = PlanoMensalidade.objects.all()

    try:
        tamLista = len(list_plans)
    except:
        context = {
            'list': list_plans,
            'tamLista': 0
        }

        return render(request, "monthlyplans/index.html", context)

    tamLista = len(list_plans)
    context = {
        'list': list_plans,
        'tamLista': tamLista
    }

    return render(request, "monthlyplans/index.html", context)


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'monthlyplans/add.html',
                  {'form': MonthlyPlansForm()})


@login_required
def create(request):
    form = MonthlyPlansForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'monthlyplans/add.html', {'form': form})

    form.save()
    return HttpResponseRedirect(r('monthlyplans:success'))


@login_required
def editPlano(request, pk):
    plano = get_object_or_404(PlanoMensalidade, pk=pk)
    form = MonthlyPlansForm(request.POST or None, instance=plano)
    if not form.is_valid():
        return render(request, 'monthlyplans/edit.html', {'form': form, 'plano': plano})
    else:
        form.save()
        return HttpResponseRedirect(r('monthlyplans:success'))


@login_required
def success(request):
    return render(request, 'monthlyplans/monthlyplans_success.html')


@login_required
def delDataModalPlano(request):
    id_list = []
    if request.is_ajax():
        select = request.POST.getlist('valores[]')

        for pk in select:
            id_list.append(int(pk))

    planos = PlanoMensalidade.objects.filter(pk__in=id_list, ativo=True)

    return render(request, 'monthlyplans/removeModal.html', {'planos': planos})


def delConfirmePlano(request, *args, **kwargs):
    select = request.POST.getlist('valores_list[]')
    for valor in select:
        PlanoMensalidade.objects.filter(pk=valor).update(ativo=False)

    return HttpResponseRedirect(r('monthlyplans:list'))


# def deleteAtleta(request, pk):
#     plano = get_object_or_404(PlanoMensalidade, pk=pk)
#     if request.method=='POST':
#         # plano.delete()
#         plano.objects.filter(pk=pk).update(ativo=False)
#         return HttpResponseRedirect(r('monthlyplans:list'))
#     return render(request, 'monthlyplans/add.html', {'object':plano})

@login_required
def fichaPlano(request, *args, **kwargs):
    idPlano = kwargs['idPlano']

    editar = True
    saveNew = False

    planos = PlanoMensalidade.objects.get(id=idPlano)
    argCode = planos.pk

    if request.method == 'GET':
        url = reverse('/inscricao/ficha/' + idPlano)
        return HttpResponseRedirect(url)
    else:

        return HttpResponseRedirect(r('monthlyplans:list'))
