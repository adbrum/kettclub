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
        print('POST')
        return create(request)
    print('GET')
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


        #
        # print('XXXX', )
        # form = SubscriptionForm(request.POST or None)  # None evita mostrar o erro no envio em branco.
        #
        # if not form.is_valid():
        #     return render(request, 'subscriptions/add.html',
        #                   {'form': form})
        #
        # if form.is_valid():
        #
        #     # Cria a instancia para ser salvo o pk na foreignkey
        #     plano = PlanoMensalidade.objects.only('pk').get(nome=form.cleaned_data['planomensalidade'])
        #
        #     Atleta.objects.create(
        #         planomensalidade=plano,
        #         nome=form.cleaned_data['nome'],
        #         sobrenome=form.cleaned_data['sobrenome'],
        #         emailatleta=form.cleaned_data['emailatleta'],
        #         datainicio=form.cleaned_data['datainicio'],
        #         datanascimento=form.cleaned_data['datanascimento'],
        #         idade=form.cleaned_data['idade'],
        #         cc=form.cleaned_data['cc'],
        #         nif=form.cleaned_data['nif'],
        #         telefone=form.cleaned_data['telefone'],
        #         telefone2=form.cleaned_data['telefone2'],
        #     )
        #
        #     return HttpResponseRedirect(r('subscriptions:list'))
        #
        # else:
        #     form = SubscriptionForm()
        #     template = "subscriptions/add.html"
        #
        # return render(request, template, {'form': form})



        # def editAtleta(request, *args, **kwargs):
        #     # Parametro recebido pelo url
        #     idAtleta = kwargs['idAtleta']
        #
        #     editar = True
        #     saveNew = False
        #
        #     atletas = Atleta.objects.get(id=idAtleta)
        #     argCode = atletas.pk
        #
        #     listaUtilizadores_filtro = []
        #     filtro = []
        #
        #     # utilizadores_filtro = Associacao_portaria_utilizador.objects.filter(portaria_id = idAtleta, \
        #     #                                 apagado = False, \
        #     #                                 ativo = True)
        #     # for i in utilizadores_filtro:
        #     #     filtro = User.objects.get(id = i.utilizador_id, \
        #     #                                     is_active = True)
        #
        #     # listaUtilizadores_filtro.append(filtro)
        #
        #     if request.method == 'POST':
        #         form = SubscriptionForm(argCode, request.POST, instance=atletas)  # An unbound form
        #
        #         # Caso Click em cancelar
        #         # Retorna para a listagem
        #         # if 'Cancelar' in request.POST or 'listaPortarias' in request.POST:
        #         #     return HttpResponseRedirect(reverse('listaPortarias'))
        #
        #         # =======================================================================
        #         # if request.POST["inp_imagem"] == "":
        #         #     img =  "/static/img/placeholder.png"
        #         # else:
        #         #     img = request.POST["inp_imagem"]
        #         # =======================================================================
        #
        #         if form.is_valid():
        #
        #             # Cria a instancia para ser salvo o pk na foreignkey
        #             plano = PlanoMensalidade.objects.only('pk').get(nome=form.cleaned_data['planomensalidade'])
        #
        #             Atleta.objects.filter(pk=idAtleta).update(
        #                 planomensalidade=plano,
        #                 nome=form.cleaned_data['nome'],
        #                 sobrenome=form.cleaned_data['sobrenome'],
        #                 emailatleta=form.cleaned_data['emailatleta'],
        #                 datainicio=form.cleaned_data['datainicio'],
        #                 datanascimento=form.cleaned_data['datanascimento'],
        #                 idade=form.cleaned_data['idade'],
        #                 cc=form.cleaned_data['cc'],
        #                 nif=form.cleaned_data['nif'],
        #                 telefone=form.cleaned_data['telefone'],
        #                 telefone2=form.cleaned_data['telefone2']
        #             )
        #
        #             return HttpResponseRedirect(r('subscriptions:list'))
        #
        #     else:
        #         form = SubscriptionForm()
        #         template = "subscriptions/add.html"
        #
        #         return render(request, template, {'form': form})


        # else:
        #     form = SubscriptionForm()
        #     template = "subscriptions/add.html"
        #
        #     return render(request, template, {'form': form})

#
# def create(request):
#     # logout(request)
#     form = SubscriptionForm(request.POST or None)  # None evita mostrar o erro no envio em branco.
#     username = request.POST['username']
#     password = request.POST['password']
#
#     if not form.is_valid():
#         return render(request, 'subscriptions/add.html',
#                       {'form': form})
#
#     if request.method == 'POST':
#         print('POST')
#         form = SubscriptionForm(request.POST)
#
#
#         if "checkValues" in request.POST:
#             listaAtletas = request.POST.getlist("checkValues")
#
#             listaAtletas_filtro = Atleta.objects.filter(id__in = listaAtletas)
#
#             atleta = Atleta.objects.all()
#
#     if user is not None:
#         if user.is_active:
#             # login(request, user)
#             try:
#                 user_ = User.objects.get(username=username)
#                 empty = Movement.objects.get(user=user_.pk, check_out__isnull=True)
#                 if empty:
#                     Movement.objects.filter(pk=empty.pk).update(check_out=datetime.now())
#                 # Redirect to a success page.
#                 print("User is valid, active and authenticated")
#                 # logout(request)
#                 return HttpResponseRedirect(r('movimentos:detail', user_.pk, 'Saida'))
#             except:
#                 Movement.objects.create(user=user)
#                 # logout(request)
#                 return HttpResponseRedirect(r('movimentos:detail', user_.pk, 'Entrada'))
#
#         else:
#             # Return a 'disabled account' error message
#             print("The password is valid, but the account has been disabled!")
#     else:
#         # Return an 'invalid login' error message.
#         print("The username and password were incorrect.")
#         return HttpResponseRedirect(r('movimentos:detail', 0, 0))



# def detail(request, pk, estado):
#     path = 'movimentos/movement_success.html'
#     print('ESTADO: ', estado)
#
#     try:
#         employee = User.objects.get(pk=pk)
#     except Movement.DoesNotExist:
#         raise Http404
#
#     return render(request, path, {'full_name': employee.get_full_name(), 'estado': estado})



# # @cache_page(60)
# def create(request, *args, **kwargs):
#     checkValues = request.POST.getlist('checkValues')
#
#     print('POSTTTTTTTTTTTT', request.POST)
#     print('GETTTTTTTTTTT', request.GET)
#
#     if request.method == 'POST':
#         print('POST')
#         # form = SubscriptionForm(request.POST)
#         #
#         #
#         # if "checkValues" in request.POST:
#         #     listaAtletas = request.POST.getlist("checkValues")
#         #
#         #     listaAtletas_filtro = Atleta.objects.filter(id__in = listaAtletas)
#         #
#         #     atleta = Atleta.objects.all()
#     else:
#         print('GET')
#         return render(request, 'subscriptions/add.html', {'form': SubscriptionForm()})
#         #
#         #
#     if request.POST["inp_imagem"] == "":
#         img = "/static/img/placeholder.png"
#     else:
#         img = request.POST["inp_imagem"]


#     # Caso Click em cancelar
#     # Retorna para a listagem
#     if 'Cancelar' in request.POST or "listColab_resid_post" in request.POST:
#         return HttpResponseRedirect(reverse('list_colab_resid'))
#
#     if form.is_valid():
#         tableColabResid = Coloboradores_Residentes(
#                             apelido = form.cleaned_data['apelido'],
#                             primeiroNome = form.cleaned_data['primeiroNome'],
#                             morada = form.cleaned_data['morada'],
#                             localidade = form.cleaned_data['localidade'],
#                             codPostal = form.cleaned_data['codPostal'],
#                             descricaoPostal = form.cleaned_data['descricaoPostal'],
#                             pais = form.cleaned_data['pais'],
#                             telefone = form.cleaned_data['telefone'],
#                             fax = form.cleaned_data['fax'],
#                             dTNascimento = form.cleaned_data['dTNascimento'],
#                             nacionalidade = form.cleaned_data['nacionalidade'],
#                             tipoDocIdentif = form.cleaned_data['tipoDocIdentif'],
#                             numDocIdentif = form.cleaned_data['numDocIdentif'],
#                             validade = form.cleaned_data['validade'],
#                             sexo = form.cleaned_data['sexo'],
#                             entEmissora = form.cleaned_data['entEmissora'],
#                             email = form.cleaned_data['email'],
#                             webPage = form.cleaned_data['webPage'],
#                             entidade = form.cleaned_data['entidade'],
#                             imagem = img,
#                             dataHoraCriacao = dateTime_actual(),
#                             utilizadorCriacao = request.user,
#                             dataHoraAlteracao = dateTime_actual(),
#                             utilizadorAlteracao = request.user,
#                             ativo = True,
#                             apagado = False,
#                             )
#         tableColabResid.save()
#
#         #Faz a associação das viaturas com os Colab/Res
#         for valor in checkValues:
#             tableViatura_col_res = Viatura_colaborador_residente(
#                                 colaboradorResidente = Coloboradores_Residentes.objects.get(id = tableColabResid.id),
#                                 viatura = Viatura.objects.get(id = valor),
#                                 dataHoraCriacao = dateTime_actual(),
#                                 utilizadorCriacao = request.user,
#                                 dataHoraAlteracao = dateTime_actual(),
#                                 utilizadorAlteracao = request.user,
#                                 ativo = True,
#                                 apagado = False
#                                 )
#             tableViatura_col_res.save()
#             Viatura.objects.filter(id = valor).update(associado = True),
#
#         #tableViatura_col_res = add_colab_res_veiculos(request, tableColabResid, listaVeiculos_filtro)
#         #tableViatura_col_res.save()
#
#         if 'SaveAndNew' in request.POST:
#             template = "gestvisitor/colab_resid/add_colab_resid.html"
#             form = AddColab_resid()
#         else:
#             return HttpResponseRedirect(reverse('list_colab_resid'))
#
#     else:
#         template = "gestvisitor/colab_resid/add_colab_resid.html"
#
# else:
#     img = "/static/img/placeholder.png"
#     form = AddColab_resid()
#     template = "gestvisitor/colab_resid/add_colab_resid.html"
#
#
# return render_to_response(template,
#     locals(),
#     context_instance = RequestContext(request),
#     )
# else:
#     print('FFFFFFFFFFFFFFFFFFFFFFFFF')
#     return render(request, 'subscriptions/subscription_form.html',
#               {'form': SubscriptionForm()})
