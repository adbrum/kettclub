from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import resolve_url as r
from django.views.decorators.cache import cache_page
from kettclub.core.models import Atleta, PlanoMensalidade
from kettclub.subscriptions.forms import SubscriptionForm, EditSubscriptionForm


@cache_page(60)
@login_required
def listsubscription(request, *args, **kwargs):
    list_subscription = Atleta.objects.all()
    tamLista = len(list_subscription)

    context = {
        'list': list_subscription,
        'tamLista': tamLista
    }

    return render(request, "subscriptions/index.html", context)


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/add.html',
                  {'form': SubscriptionForm()})


def empty_prototipo_form(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})


@login_required
def create(request):
    form = SubscriptionForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'subscriptions/add.html', {'form': form})
    else:
        form.save()
        return HttpResponseRedirect(r('subscriptions:list'))


@login_required
def editAtleta(request, pk):
    atleta = get_object_or_404(Atleta, pk=pk)
    form = EditSubscriptionForm(request.POST or None, instance=atleta)
    if not form.is_valid():
        return render(request, 'subscriptions/edit.html', {'form': form, 'atleta': atleta})
    else:
        form.save()
        return HttpResponseRedirect(r('subscriptions:list'))


@login_required
def delDataModalAtleta(request):
    id_list = []
    if request.is_ajax():
        select = request.POST.getlist('valores[]')

        for pk in select:
            id_list.append(int(pk))

    atletas = Atleta.objects.filter(pk__in=id_list, ativo=True)

    return render(request, 'subscriptions/removeModal.html', {'atletas': atletas})


@login_required
def delConfirmeAtleta(request, *args, **kwargs):
    select = request.POST.getlist('valores_list[]')
    for valor in select:
        Atleta.objects.filter(pk=valor).update(ativo=False)

    return HttpResponseRedirect(r('subscriptions:list'))


# def deleteAtleta(request, pk):
#     atleta = get_object_or_404(Atleta, pk=pk)
#     if request.method=='POST':
#         # atleta.delete()
#         atleta.objects.filter(pk=pk).update(ativo=False)
#         return HttpResponseRedirect(r('subscriptions:list'))
#     return render(request, 'subscriptions/add.html', {'object':atleta})


def fichaAtleta(request, *args, **kwargs):
    idAtleta = kwargs['idAtleta']

    editar = True
    saveNew = False

    atletas = Atleta.objects.get(id=idAtleta)
    argCode = atletas.pk

    if request.method == 'GET':
        url = reverse('/inscricao/ficha/' + idAtleta)
        return HttpResponseRedirect(url)
    else:

        return HttpResponseRedirect(r('subscriptions:list'))

