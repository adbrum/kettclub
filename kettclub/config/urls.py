from django.conf.urls import url
from kettclub.config.view_config import configuracao
from kettclub.config.view_utilizadores import listUsers, fichaUser, resetPassword, desativarUsers, \
    confirmDesativarUsers, \
    ativarUsers, confirmAtivarUsers, success, addUser, editUser, listGrupos, addGrupo, meuPerfil, fichaMeuPerfil, \
    editGrupo, fichaGrupo, confirmApagarGrupos, apagarGrupo

urlpatterns = [
    url(r'^sucesso/', success, name='success'),

    # Menu Configuração
    url(r'^$', configuracao, name="config"),

    # Listagem Utilizadores
    url(r'^users/$', listUsers, name="listUsers"),

    # Criar Utilizador
    url(r'^users/add/$', addUser, name="addUser"),

    # Editar Utilizador
    url(r'^users/edit/(?P<idUser>\d+)/$', editUser, name="editUser"),

    # Ficha Utilizador
    url(r'^users/view/(?P<idUser>\d+)/$', fichaUser, name="fichaUser"),

    # Desativar Utilizador
    url(r'^users/des/confirm/(?P<listUsers>\w+)/$', desativarUsers,
        name="desativarUsers"),

    # Confirmar Desativar Utilizador
    url(r'^users/des/confirm/$', confirmDesativarUsers,
        name="confirmDesativarUsers"),

    # Ativar Utilizador
    url(r'^users/act/confirm/(?P<listUsers>\w+)/$', ativarUsers,
        name="ativarUsers"),

    # Confirmar Ativar Utilizador
    url(r'^users/act/confirm/$', confirmAtivarUsers,
        name="confirmAtivarUsers"),

    # Ativar Utilizador
    url(r'^users/reset/pwd/(?P<idUser>\d+)/$', resetPassword,
        name="resetPassword"),

    # Listagem de Grupos de Utilizador
    url(r'^users/grupo/$', listGrupos, name="listGrupos"),

    # Criar Grupo de Utilizadores
    url(r'^users/grupo/add/$', addGrupo, name="addGrupo"),

    # Editar Grupo de Utilizador
    url(r'^users/grupo/edit/(?P<idGroup>\d+)/$', editGrupo,
        name="editGrupo"),

    # Ficha Grupo de Utilizador
    url(r'^users/grupo/view/(?P<idGroup>\d+)/$', fichaGrupo,
        name="fichaGrupo"),

    # Apagar Grupo
    url(r'^users/grupo/del/confirm/(?P<listGrupos>\w+)/$', apagarGrupo,
        name="apagarGrupo"),

    # Confirmar Apagar Grupo
    url(r'^users/grupo/del/confirm/$', confirmApagarGrupos,
        name="confirmApagarGrupos"),

    # Meu Perfil
    url(r'^settings/perfil/(?P<idUser>\d+)/$', meuPerfil, name="meuPerfil"),

    # Ficha Meu Perfil
    url(r'^settings/perfil/view/(?P<idUser>\d+)/$', fichaMeuPerfil,
        name="fichaMeuPerfil"),

]
