from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import resolve_url as r
from kettclub.monthlyplans.models import PlanoMensalidade

from kettclub.subscriptions.forms import SubscriptionForm, EditSubscriptionForm
from kettclub.subscriptions.models import Subscription


@login_required
def listsubscription(request, *args, **kwargs):
    list_ = PlanoMensalidade.objects.all()

    if list_:
        data = Subscription.objects.all()
        if not data:
            context = {
                'list': data,
                'tamLista': 0,
            }

            return render(request, "subscriptions/index.html", context)
        else:
            context = {
                'list': data,
                'tamLista': 1,
            }

            return render(request, "subscriptions/index.html", context)
    else:
        context = {
            'list_': 0
        }

        return render(request, "subscriptions/index.html", context)
    # try:
    #     tamLista = len(list_subscription)
    # except:
    #     context = {
    #         'list': list_subscription,
    #         'tamLista': 0
    #     }
    #
    #     return render(request, "subscriptions/index.html", context)

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
    # saveNew = True
    form = SubscriptionForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'subscriptions/add.html', locals())
    else:
        form.save()
        return HttpResponseRedirect(r('subscriptions:success'))


@login_required
def editSubscription(request, pk):
    atleta = get_object_or_404(Subscription, pk=pk)
    form = EditSubscriptionForm(request.POST or None, instance=atleta)
    if not form.is_valid():
        return render(request, 'subscriptions/edit.html', {'form': form, 'atleta': atleta})
    else:
        form.save()
        return HttpResponseRedirect(r('subscriptions:success'))


@login_required
def success(request):
    return render(request, 'subscriptions/subscription_success.html')


@login_required
def delDataModalSubscription(request):
    id_list = []
    if request.is_ajax():
        select = request.POST.getlist('valores[]')

        for pk in select:
            id_list.append(int(pk))

    atletas = Subscription.objects.filter(pk__in=id_list, ativo=True)

    return render(request, 'subscriptions/removeModal.html', {'atletas': atletas})


@login_required
def delConfirmeSubscription(request, *args, **kwargs):
    select = request.POST.getlist('valores_list[]')
    for valor in select:
        Subscription.objects.filter(pk=valor).update(ativo=False)

    return HttpResponseRedirect(r('subscriptions:list'))


# def deleteSubscription(request, pk):
#     atleta = get_object_or_404(Subscription, pk=pk)
#     if request.method=='POST':
#         # atleta.delete()
#         atleta.objects.filter(pk=pk).update(ativo=False)
#         return HttpResponseRedirect(r('subscriptions:list'))
#     return render(request, 'subscriptions/add.html', {'object':atleta})


def fichaSubscription(request, *args, **kwargs):
    idSubscription = kwargs['idSubscription']

    editar = True
    saveNew = False

    atletas = Subscription.objects.get(id=idSubscription)
    argCode = atletas.pk

    if request.method == 'GET':
        url = reverse('/inscricao/ficha/' + idSubscription)
        return HttpResponseRedirect(url)
    else:

        return HttpResponseRedirect(r('subscriptions:list'))
