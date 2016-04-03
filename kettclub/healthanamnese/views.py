from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import resolve_url as r
from kettclub.healthanamnese.forms import HealthAnamneseForm, EditHealthAnamneseForm
from kettclub.healthanamnese.models import SaudeAnamnese


@login_required
def listhealthanamnese(request, *args, **kwargs):
    list_healthanamnese = SaudeAnamnese.objects.all()

    try:
        tamLista = len(list_healthanamnese)
    except:
        context = {
            'list': list_healthanamnese,
            'tamLista': 0
        }

        return render(request, "healthanamnese/index.html", context)

    tamLista = len(list_healthanamnese)
    context = {
        'list': list_healthanamnese,
        'tamLista': tamLista
    }

    return render(request, "healthanamnese/index.html", context)


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'healthanamnese/add.html',
                  {'form': HealthAnamneseForm()})


def empty_prototipo_form(request):
    return render(request, 'healthanamnese/healthanamnese_form.html',
                  {'form': HealthAnamneseForm()})


@login_required
def create(request):
    # saveNew = True
    form = HealthAnamneseForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'healthanamnese/add.html', locals())
    else:
        form.save()
        return HttpResponseRedirect(r('healthanamnese:success'))


@login_required
def editSaudeAnamnese(request, pk):
    saude_anamnese = get_object_or_404(SaudeAnamnese, pk=pk)
    form = EditHealthAnamneseForm(request.POST or None, instance=saude_anamnese)
    if not form.is_valid():
        return render(request, 'healthanamnese/edit.html', {'form': form, 'saude_anamnese': saude_anamnese})
    else:
        form.save()
        return HttpResponseRedirect(r('healthanamnese:success'))


@login_required
def success(request):
    return render(request, 'healthanamnese/healthanamnese_success.html')


@login_required
def delConfirmeSaudeAnamnese(request, *args, **kwargs):
    select = request.POST.getlist('valores_list[]')
    for valor in select:
        SaudeAnamnese.objects.filter(pk=valor).update(ativo=False)

    return HttpResponseRedirect(r('healthanamnese:list'))


# def deleteSaudeAnamnese(request, pk):
#     saude_anamnese = get_object_or_404(SaudeAnamnese, pk=pk)
#     if request.method=='POST':
#         # saude_anamnese.delete()
#         saude_anamnese.objects.filter(pk=pk).update(ativo=False)
#         return HttpResponseRedirect(r('healthanamnese:list'))
#     return render(request, 'healthanamnese/add.html', {'object':saude_anamnese})


def fichaSaudeAnamnese(request, *args, **kwargs):
    idSaudeAnamnese = kwargs['idSaudeAnamnese']

    editar = True
    saveNew = False

    saude_anamneses = SaudeAnamnese.objects.get(id=idSaudeAnamnese)
    argCode = saude_anamneses.pk

    if request.method == 'GET':
        url = reverse('/inscricao/ficha/' + idSaudeAnamnese)
        return HttpResponseRedirect(url)
    else:

        return HttpResponseRedirect(r('healthanamnese:list'))

