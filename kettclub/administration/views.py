import collections
from datetime import datetime
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r, redirect
from kettclub.core.models import Presenca, Atleta
from kettclub.administration.forms import LoginForm


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'administration/login_form.html', {'form': form})

        username = request.POST['username']
        password = request.POST['password']

        if '@' in username:  # se tiver @ no nome do usuário  username vai ser o email
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            # tentando buscar o usuário no banco
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                user = authenticate(username=user.username, password=password)
                login(request, user)
                return HttpResponseRedirect(r('administration:dash'))
        except User.DoesNotExist:
            return render(request, 'administration/login_form.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'administration/login_form.html', {'form': form})


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# @cache_page(60)
@login_required
def dash(request):
    now = datetime.now()

    # print('RRRRRRRRRRRRRRRRRRRRRRR', pk)
    # dmin = request.POST.get('date1')
    # dmax = request.POST.get('date2')
    min_date = datetime.strptime('01/03/2016', "%d/%m/%Y")
    max_date = datetime.strptime('21/03/2016', "%d/%m/%Y")
    # top20 = Presenca.objects.annotate(Count('numeroatleta')).filter(datapresenca__gte=min_date,
    #                                                                 datapresenca__lte=max_date).order_by(
    #     '-numeroatleta__count')[:20]
    presenca = Presenca.objects.filter(datapresenca=datetime.today()).count()

    # teste = Presenca.objects.filter(numeroatleta__gte=Presenca.objects.order_by('-numeroatleta')[5].numeroatleta )

    topT = Presenca.objects.values('nome').annotate(numeroatleta_count=Count('numeroatleta')).filter(
        datapresenca__gte=min_date,
        datapresenca__lte=max_date).order_by('-numeroatleta_count')[:20]

    # top_scores = (Presenca.objects
    #                  .order_by('-numeroatleta')
    #                  .values_list('numeroatleta', flat=True)
    #                  .distinct())
    # top_records = (Presenca.objects
    #                   .order_by('numeroatleta')
    #                   .filter(numeroatleta__in=top_scores[:10]))


    # presenca = Presenca.objects.filter(datapresenca__gte=min_date, datapresenca__lte=max_date).count()

    # print('NUMERO ATLETA X: ', teste)
    # print('NUMERO ATLETA 20X: ', top20)
    # print('NUMERO ATLETA teste2X: ', topT)
    # print('NUMERO ATLETA top_records: ', top_records)
    #
    # top = []
    # nomealuno = []
    #
    # for i in top20:
    #     top.append(i.numeroatleta)
    #
    # for i in nomealuno:
    #     print(i)
    #
    # top20 = list(set(top))
    #
    #
    # c = collections.Counter(top)
    #
    # revDct = dict((key, val) for (key, val) in c.most_common(20))
    #
    #
    # changedDict = {}
    #
    # for key, elem in revDct.items():
    #     chave = Atleta.objects.get(pk=key)
    #
    #     changedDict.update(dict((chave.nome, elem) for (key, value) in revDct.items()))

    # atleta = Atleta.objects.filter(pk__in=top20)
    novos = Atleta.objects.filter(created_at__month=now.month).count()
    qtmes = Presenca.objects.filter(created_at__month=now.month).count()

    context = {'presencas': presenca,
               'top': topT,
               # 'atletas': atleta,
               # 'chan': changedDict,
               'mes': qtmes,
               'novos': novos}

    return render(request, 'administration/index.html', context)





    # @login_required

# def Login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#
#         if not form.is_valid():
#             return render(request, 'administration/login_form.html', {'form': form})
#
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             # the password verified for the user
#             if user.is_active:
#                 login(request, user)
#                 print("User is valid, active and authenticated")
#                 # return HttpResponseRedirect(r('administration:dash', user.pk))
#                 return HttpResponseRedirect(r('administration:dash'))
#             else:
#                 print("The password is valid, but the account has been disabled!")
#         else:
#             form = LoginForm()
#             return render(request, 'administration/login_form.html', {'form': form})
#     else:
#         form = LoginForm()
#         return render(request, 'administration/login_form.html', {'form': form})



#
# def get_user(self, user_id):  # sobreescrita do metodo get_user, que é usado para retorna o usuário logado no sistema
#
#     try:
#
#         user = User.objects.get(pk=user_id)
#
#     except User.DoesNotExist:
#
#         return None

#
