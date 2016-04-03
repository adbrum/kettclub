from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import resolve_url as r
from kettclub.reviewsphysicals.forms import EvaluationForm, EditEvaluationForm
from kettclub.reviewsphysicals.models import Avaliacao
from kettclub.subscriptions.models import Atleta


@login_required
def listavaliacao(request, *args, **kwargs):
    list_ = Atleta.objects.all()

    if list_:
        data = Avaliacao.objects.filter()
        if not data:
            context = {
                'list': data,
                'tamLista': 0,
            }

            return render(request, "reviewsphysicals/index.html", context)
        else:
            context = {
                'list': data,
                'tamLista': 1,
            }

            return render(request, "reviewsphysicals/index.html", context)
    else:
        context = {
            'list_': 0
        }

        return render(request, "reviewsphysicals/index.html", context)


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'reviewsphysicals/add.html',
                  {'form': EvaluationForm()})


def empty_prototipo_form(request):
    return render(request, 'reviewsphysicals/evaluation_form.html',
                  {'form': EvaluationForm()})


@login_required
def create(request):
    form = EvaluationForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'reviewsphysicals/add.html', {'form': form})
    else:
        form.save()
        return HttpResponseRedirect(r('reviewsphysicals:success'))


@login_required
def editAvaliacao(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    form = EditEvaluationForm(request.POST or None, instance=avaliacao)
    if not form.is_valid():
        return render(request, 'reviewsphysicals/edit.html', {'form': form, 'avaliacao': avaliacao})
    else:
        form.save()
        return HttpResponseRedirect(r('reviewsphysicals:success'))


@login_required
def success(request):
    return render(request, 'reviewsphysicals/avaliation_success.html')


# def editAvaliacao(request, pk):
# avaliacao = get_object_or_404(Avaliacao, pk=pk)
# form = EditEvaluationForm(request.POST or None, instance=avaliacao)
# if not form.is_valid():
#     return render(request, 'reviewsphysicals/edit.html', {'form': form, 'avaliacao': avaliacao})
# else:
#     form.save()
#     return HttpResponseRedirect(r('reviewsphysicals:list'))


@login_required
def delDataModalAvaliacao(request):
    id_list = []
    if request.is_ajax():
        select = request.POST.getlist('valores[]')

        for pk in select:
            id_list.append(int(pk))

    avaliacoes = Avaliacao.objects.filter(pk__in=id_list, ativo=True)

    return render(request, 'reviewsphysicals/removeModal.html', {'avaliacoes': avaliacoes})


@login_required
def delConfirmeAvaliacao(request, *args, **kwargs):
    select = request.POST.getlist('valores_list[]')
    for valor in select:
        Avaliacao.objects.filter(pk=valor).update(ativo=False)

    return HttpResponseRedirect(r('reviewsphysicals:list'))


# def deleteAvaliacao(request, pk):
#     avaliacao = get_object_or_404(Avaliacao, pk=pk)
#     if request.method=='POST':
#         # avaliacao.delete()
#         avaliacao.objects.filter(pk=pk).update(ativo=False)
#         return HttpResponseRedirect(r('reviewsphysicals:list'))
#     return render(request, 'reviewsphysicals/add.html', {'object':avaliacao})


def fichaAvaliacao(request, *args, **kwargs):
    idAvaliacao = kwargs['idAvaliacao']

    editar = True
    saveNew = False

    avaliacoes = Avaliacao.objects.get(id=idAvaliacao)
    argCode = avaliacoes.pk

    if request.method == 'GET':
        url = reverse('/avaliacao/ficha/' + idAvaliacao)
        return HttpResponseRedirect(url)
    else:

        return HttpResponseRedirect(r('reviewsphysicals:list'))
