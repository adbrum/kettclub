from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import resolve_url as r
from kettclub.healthanamnese.models import SaudeAnamnese
from kettclub.monthlyplans.models import PlanoMensalidade

from kettclub.externalapplication.forms import SubscriptionForm, HealthAnamneseForm
from kettclub.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        print('POST')
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'externalapplication/add.html',
                  {'form': SubscriptionForm(), 'form_02': HealthAnamneseForm()})


def empty_prototipo_form(request):
    return render(request, 'externalapplication/subscription_form.html',
                  {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST or None)
    form_02 = HealthAnamneseForm(request.POST or None)

    if not (form.is_valid() or form_02.is_valid()):
        return render(request, 'externalapplication/add.html', locals())

    elif form.is_valid() and form_02.is_valid():
        atleta = Subscription.objects.create(**form.cleaned_data)

        SaudeAnamnese.objects.create(atleta_id=atleta.pk,
                                     quest01=form_02.cleaned_data['quest01'], quest02=form_02.cleaned_data['quest02'],
                                     quest03=form_02.cleaned_data['quest03'], quest04=form_02.cleaned_data['quest04'],
                                     quest05=form_02.cleaned_data['quest05'], quest06=form_02.cleaned_data['quest06'],
                                     quest07=form_02.cleaned_data['quest07'], quest08=form_02.cleaned_data['quest08'],
                                     quest09=form_02.cleaned_data['quest09'], quest010=form_02.cleaned_data['quest010'],
                                     quest011=form_02.cleaned_data['quest011'],
                                     quest012=form_02.cleaned_data['quest012'],
                                     quest013=form_02.cleaned_data['quest013'],
                                     quest014=form_02.cleaned_data['quest014'],
                                     quest015=form_02.cleaned_data['quest015'],
                                     quest016=form_02.cleaned_data['quest016'],
                                     quest017=form_02.cleaned_data['quest017'],
                                     quest018=form_02.cleaned_data['quest018'],
                                     quest019=form_02.cleaned_data['quest019'],
                                     quest020=form_02.cleaned_data['quest020'],
                                     quest021=form_02.cleaned_data['quest021'],
                                     quest022=form_02.cleaned_data['quest022'],
                                     quest023=form_02.cleaned_data['quest023']
                                     )
        # form.save()
        return HttpResponseRedirect(r('external:success'))


def success(request):
    return render(request, 'externalapplication/subscription_success.html')
