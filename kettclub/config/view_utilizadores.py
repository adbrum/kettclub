from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group, Permission
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from django.utils.translation import ugettext_lazy as _
from kettclub.config.form_utilizadores import AddUserForm, AddGroupForm, \
    EditUserForm, PasswordChangeFormReset, EditGroupForm, MeuPerfilForm, \
    FichaUserForm, FichaGroupForm, FichaMeuPerfilForm


@login_required
def success(request):
    return render(request, 'config/success.html')


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.list_user' in list(user.get_all_permissions()),
                  login_url='redirect')
def listUsers(request):
    """
    Listar todos os utilizadores exceto superuser e staff.
    :param request:
    :return:
    """
    utilizadores = User.objects.filter().exclude(is_superuser=True, is_staff=True)

    teste = user_passes_test(lambda user: '.add_subscription' in list(user.get_all_permissions()))

    # print("all_permissions", list(request.user.get_all_permissions()))

    # tamLista = len(utilizadores)

    if not utilizadores:
        context = {
            'utilizadores': utilizadores,
            'tamLista': 0,
        }

        return render(request, "config/index.html", context)
    else:
        context = {
            'utilizadores': utilizadores,
            'tamLista': 1,
        }

        return render(request, "config/index.html", context)


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.add_user' in list(user.get_all_permissions()),
                  login_url='redirect')
def addUser(request):
    """
    Adicionar Utilizadores
    :param request:
    :return:
    """

    saveNew = False

    perfis = Group.objects.all()

    listaErros = []
    warning = False
    if len(perfis) == 0:
        warning = True
        warningMensage = _(u'Atenção deve criar perfis de utilizador antes das criação de um utilizador!')
        listaErros.append(warningMensage)

    if request.method == 'POST':
        form = AddUserForm(request.POST)

        if form.is_valid():

            tableuser = User(username=form.cleaned_data['username'],
                             first_name=form.cleaned_data['p_nome'],
                             last_name=form.cleaned_data['u_nome'],
                             email=form.cleaned_data['e_mail'],
                             password=form.cleaned_data['pwd'],
                             )

            # encripta a pwd
            tableuser.set_password(form.cleaned_data['pwd'])

            tableuser.save()

            # # LOG App
            # guardarLogs("I", dateTime_actual(), request.user, \
            #             "Inserir utilizador " + str(tableuser.id))

            # Relaciona os grupos com o user
            for c in form.cleaned_data['grupos']:
                # relaciona a permissao ao grupo
                g = Group.objects.get(name=c.name)

                # get last id inserted
                last_id = User.objects.latest('id')
                # atualiza na db
                g.user_set.add(last_id)

            if 'SaveAndNew' in request.POST:
                form = AddUserForm()
                return render(request, "config/addUser.html", locals())

            return HttpResponseRedirect(reverse('config:success'))

        else:
            warning = True
            warningMensage = _(u'Atenção existem campos por preencher!')
            listaErros.append(warningMensage)
            template = "config/addUser.html"

    else:
        form = AddUserForm()

        return render(request, 'config/addUser.html', locals())


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.edit_user' in list(user.get_all_permissions()),
                  login_url='redirect')
def editUser(request, *args, **kwargs):
    """
    Editar Utilizadores
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    # Parametro recebido pelo url
    idUser = kwargs['idUser']
    listaErros = []
    utilizador = User.objects.get(id=idUser)

    argUser = utilizador.username
    argEmail = utilizador.email

    listaGrupos = utilizador.groups.all()

    if request.method == 'POST':
        form = EditUserForm(argUser, argEmail, listaGrupos, request.POST, instance=utilizador)  # An unbound form
        if form.is_valid():
            User.objects.filter(id=idUser).update(username=form.cleaned_data['username'],
                                                  first_name=form.cleaned_data['first_name'],
                                                  last_name=form.cleaned_data['last_name'],
                                                  email=form.cleaned_data['email'],
                                                  )

            # LOG App
            # guardarLogs("U", dateTime_actual(), request.user, \
            #             "Update utilizador " + str(idUser))
            #
            # Apaga os grupos do utilizador
            for d in utilizador.groups.all():
                g = Group.objects.get(name=d)
                g.user_set.remove(idUser)

            # Associa os grupos ao utilizador
            for d in form.cleaned_data['grupos']:
                g = Group.objects.get(name=d)
                g.user_set.add(idUser)

            if 'SaveAndNew' in request.POST:
                form = AddUserForm()
                return render_to_response("config/addUser.html",
                                          locals(),
                                          context_instance=RequestContext(request),
                                          )

            messages.success(request, "Edição realizada com sucesso!")

            return HttpResponseRedirect(reverse('config:success'))
    else:
        form = EditUserForm(argUser, argEmail, listaGrupos, instance=utilizador)  # An unbound form

    return render(request, 'config/editUser.html', locals())


# @user_passes_test(lambda u: u".edit_user" in list(u.get_all_permissions()), login_url="redirectNaoAuto")
def fichaUser(request, *args, **kwargs):
    """
    Mostrar dados do Utilizador
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    # Parametro recebido pelo url
    idUser = kwargs['idUser']
    listaErros = []

    utilizador = User.objects.get(id=idUser)

    if request.method == 'POST':
        url = reverse('config:editUser', kwargs={'idUser': idUser})
        return HttpResponseRedirect(url)
    else:
        form = FichaUserForm(utilizador.groups.all(), instance=utilizador)

    return render(request, "config/addUser.html", locals())


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.delete_user' in list(user.get_all_permissions()),
                  login_url='redirect')
def desativarUsers(request, *args, **kwargs):
    """
    Desativar Utilizadores
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    usersSelected = kwargs['listUsers']
    listIdUser = usersSelected.split("_")
    listIdUser.pop()

    for idUser in listIdUser:
        User.objects.filter(id=idUser).update(is_active=False,
                                              )
        # LOG App
        # guardarLogs("U", dateTime_actual(), request.user, \
        #             "Desativar utilizador " + str(idUser))
        #
    return HttpResponseRedirect(reverse('config:listUsers'))


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.delete_user' in list(user.get_all_permissions()),
                  login_url='redirect')
def confirmDesativarUsers(request, *args, **kwargs):
    """
    Confirmar a desativação dos utilizadores
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    if request.is_ajax():
        try:
            request.POST["valores[]"]  # obriga ao except
            lUsers_id = []
            strUrl = ""
            for user_id in request.POST.getlist("valores[]"):
                utilizadores = User.objects.filter(id=user_id)
                for u in utilizadores:
                    lUsers_id.append(u.username)
                    strUrl += str(u.id) + "_"
                var = 0
                context = {
                    'lUsers_id': lUsers_id
                }
        except:
            message = _(u'Deve selecionar pelo menos um utilizador!')

    return render(request, 'config/desativarModal.html', locals())



@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.add_user' in list(user.get_all_permissions()),
                  login_url='redirect')
def ativarUsers(request, *args, **kwargs):
    """
    Ativar os utilizadores selecionados
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    usersSelected = kwargs['listUsers']
    listIdUser = usersSelected.split("_")
    listIdUser.pop()

    for idUser in listIdUser:
        User.objects.filter(id=idUser).update(is_active=True,
                                              )

        # LOG App
        # guardarLogs("U", dateTime_actual(), request.user, \
        #             "Ativar utilizador " + str(idUser))

    return HttpResponseRedirect(reverse('config:listUsers'))


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.add_user' in list(user.get_all_permissions()),
                  login_url='redirect')
def confirmAtivarUsers(request, *args, **kwargs):
    """
    Confirmar a ativação dos utilizadores selecionados
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    if request.is_ajax():
        try:
            request.POST["valores[]"]  # obriga ao except
            lUsers_id = []
            strUrl = ""
            for user_id in request.POST.getlist("valores[]"):
                utilizadores = User.objects.filter(id=user_id)
                for u in utilizadores:
                    lUsers_id.append(u.username)
                    strUrl += str(u.id) + "_"
                var = 0
        except:
            message = _(u'Deve selecionar pelo menos um utilizador!')

    return render(request, 'config/ativarModal.html', locals())


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.list_user' in list(user.get_all_permissions()),
                  login_url='redirect')
def resetPassword(request, *args, **kwargs):
    """
    Fazer reset a password
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    # pathLogo = pathLogotipo()
    # listaInfo = statusIcon(request)
    #
    idUser = kwargs["idUser"]
    userEdit = User.objects.get(id=idUser)

    nomeUser = userEdit.username

    password_change_form = PasswordChangeFormReset
    if request.method == "POST":
        form = password_change_form(user=userEdit, data=request.POST)
        if form.is_valid():
            form.save()

            # LOG App
            # guardarLogs("U", dateTime_actual(), request.user, \
            #             "Reset Password utilizador " + str(userEdit.id))

            # return HttpResponseRedirect(reverse('config:listUsers'))

            messages.success(request, "Password alterado com sucesso!")

            return HttpResponseRedirect(reverse('config:success'))
    else:
        form = password_change_form(user=userEdit)

    return render(request, "config/resetPassword.html", locals())


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.list_group' in list(user.get_all_permissions()),
                  login_url='redirect')
def listGrupos(request):
    """
    listar todos os Grupos (perfis) de utilizador
    :param request:
    :return:
    """

    perfis = Group.objects.all()

    tamLista = len(perfis)
    tamPermissoes = len(Permission.objects.filter(content_type=500))

    return render(request, "config/listGrupos.html", locals(), )


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.add_group' in list(user.get_all_permissions()),
                  login_url='redirect')
def addGrupo(request):
    """
    Adicionar um Grupo (perfil) de utilizador
    :param request:
    :return:
    """

    saveNew = False

    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            nomeGroup = form.cleaned_data['name']
            tablegroup = Group(name=nomeGroup,
                               )

            tablegroup.save()

            # # LOG App
            # guardarLogs("I", dateTime_actual(), request.user, \
            #             "Inserir Grupo de Utilizador " + str(tablegroup))

            # Relaciona as permissoes com o grupo
            for p in form.cleaned_data['perm']:
                # relaciona a permissao ao grupo
                g = Permission.objects.get(name=p.name)

                # get last id inserted
                last_id = Group.objects.latest('id')
                # atualiza na db
                g.group_set.add(last_id)

            if 'SaveAndNew' in request.POST:
                form = AddGroupForm()
                return render(request, "config/addGrupo.html",
                              locals())

            messages.success(request, "Adição realizada com sucesso!")

            return HttpResponseRedirect(reverse('config:success'))

        else:
            template = "config/addGrupo.html"

    else:
        form = AddGroupForm()

    return render(request, "config/addGrupo.html", locals())


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.edit_group' in list(user.get_all_permissions()),
                  login_url='redirect')
def editGrupo(request, *args, **kwargs):
    """
    Editar todos os Grupos (perfis) de utilizador
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    idGroup = kwargs["idGroup"]
    groupEdit = Group.objects.get(id=idGroup)

    name = groupEdit.name

    perms = groupEdit.permissions.all()

    if request.method == 'POST':
        form = EditGroupForm(perms, name, request.POST, instance=groupEdit)  # An unbound form
        if form.is_valid():
            Group.objects.filter(id=idGroup).update(name=form.cleaned_data['name'],
                                                    )

            # LOG App
            # guardarLogs("U", dateTime_actual(), request.user, \
            #             "Update Grupo de Utilizador " + str(idGroup))

            for p in perms:
                groupEdit.permissions.remove(p)

            for p in form.cleaned_data['perm']:
                groupEdit.permissions.add(p)

            if 'SaveAndNew' in request.POST:
                form = AddGroupForm()
                return render(request, "config/addGrupo.html", locals())

            messages.success(request, "Edição realizada com sucesso!")

            return HttpResponseRedirect(reverse('config:success'))
    else:
        form = EditGroupForm(perms, name, instance=groupEdit)  # An unbound form

    return render(request, "config/editGrupo.html", locals())


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.edit_group' in list(user.get_all_permissions()),
                  login_url='redirect')
def fichaGrupo(request, *args, **kwargs):
    """
    Ver as dados dos Grupos (perfis) de utilizador
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    idGroup = kwargs["idGroup"]
    groupEdit = Group.objects.get(id=idGroup)

    if request.method == 'POST':
        url = reverse('editGrupo', kwargs={'idGroup': idGroup})
        return HttpResponseRedirect(url)
    else:
        form = FichaGroupForm(groupEdit.permissions.all(), instance=groupEdit)  # An unbound form

    return render(request, "config/addGrupo.html", locals())


#
# #Função para verificar se pode ou não apagar o Grupo
@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.delete_group' in list(user.get_all_permissions()),
                  login_url='redirect')
def isApagarGrupo(perfilObj):
    '''
    Tabelas associadas: -> Utilizadores
    '''
    utilizadores = perfilObj.user_set.all().exists()
    # print "utilizadores ->", perfilObj, utilizadores
    if not utilizadores:
        return True, [], 0
    else:
        if utilizadores:
            return False, perfilObj.user_set.all(), 1


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.delete_group' in list(user.get_all_permissions()),
                  login_url='redirect')
def apagarGrupo(request, *args, **kwargs):
    """
    Apgar os Grupos (perfis) selecionados
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    perfisSelected = kwargs['listGrupos']
    listIdGrupo = perfisSelected.split("_")
    listIdGrupo.pop()

    for idGrupo in listIdGrupo:
        perfilObj = Group.objects.get(id=idGrupo)
        utilizadores = perfilObj.user_set.all()
        for u in utilizadores:
            grupos = u.groups.all()
            if len(grupos) == 1:
                User.objects.filter(id=u.id).update(is_active=False)

        Group.objects.filter(id=idGrupo).delete()
        # LOG App
        # guardarLogs("D", dateTime_actual(), request.user, \
        #             "Apagar perfil " + str(idGrupo))

    return HttpResponseRedirect(reverse('config:listGrupos'))


@login_required
@user_passes_test(lambda user: user.is_superuser or 'workout.delete_group' in list(user.get_all_permissions()),
                  login_url='redirect')
def confirmApagarGrupos(request, *args, **kwargs):
    """
    Confirmar apagar os Grupos (perfis) selecionados
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    if request.is_ajax():
        listaIdsGrupos = request.POST.getlist("valores[]")
        print("ajax", listaIdsGrupos)
        strUrl = ""
        if listaIdsGrupos != []:
            TITULO_MODAL = _(u'Aviso')
            var = 0
            podeApagar_list = []

            for id_perfil in listaIdsGrupos:
                perfilObj = Group.objects.get(id=id_perfil)
                podeApagar_list.append(perfilObj)
                isApagar = True
                PERGUNTA_0 = _(u'Do(s) Grupo(os) selecionados pode apagar os seguintes:')
                strUrl += str(id_perfil) + "_"

        else:
            TITULO_MODAL = _(u'Alerta')
            ALERTA = _(u'Deve selecionar o grupo que deseja apagar!')

        PERGUNTA = _(u'Deseja mesmo apagar o(s) grupo(s)?')

        return render(request, 'config/apagarGruposModal.html', locals())


@login_required
def meuPerfil(request, *args, **kwargs):
    """
    Meu perfil nos settings
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    # Parametro recebido pelo url
    idUser = kwargs['idUser']

    utilizador = User.objects.get(id=idUser)

    userAtual = request.user

    argUser = utilizador.username
    argEmail = utilizador.email

    if request.method == 'POST':
        form = MeuPerfilForm(argUser, argEmail, userAtual, request.POST, instance=utilizador)  # An unbound form
        if form.is_valid():
            form.save()
            User.objects.filter(id=idUser).update(username=form.cleaned_data['username'],
                                                  first_name=form.cleaned_data['first_name'],
                                                  last_name=form.cleaned_data['last_name'],
                                                  email=form.cleaned_data['email'],
                                                  )

            # # LOG App
            # guardarLogs("U", dateTime_actual(), request.user, \
            #             "Update Meu perfil " + str(idUser))

            print('SUCESSSO')

            return HttpResponseRedirect(reverse('config:success'))
    else:
        form = MeuPerfilForm(argUser, argEmail, userAtual, instance=utilizador)  # An unbound form

    return render(request, "config/edit_meu_perfil.html", locals())


@login_required
def fichaMeuPerfil(request, *args, **kwargs):
    """
    ver meu perfil nos settings
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    bEdit = True

    # Parametro recebido pelo url
    idUser = kwargs['idUser']

    utilizador = User.objects.get(id=idUser)

    if request.method == 'POST':
        print('FICAHAAAAAAAAAAA PORDT')
        # url = reverse(kwargs={'idUser': idUser})
        return HttpResponseRedirect('/config/settings/perfil/' + idUser, {'idUser': idUser})
    else:
        print('FICAHAAAAAAAAAAA')
        form = FichaMeuPerfilForm(instance=utilizador)

    return render(request, "config/meuPerfil.html", locals())
