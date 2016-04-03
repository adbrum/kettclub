from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from kettclub.administration.forms import LoginForm
from kettclub.assiduousness.models import Presenca
from kettclub.subscriptions.models import Atleta


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
    now = datetime.now().date()

    if request.method == 'POST':
        dmin = request.POST.get('date1')
        dmax = request.POST.get('date2')

        min_date = datetime.strptime(dmin, "%d/%m/%Y")
        max_date = datetime.strptime(dmax, "%d/%m/%Y")
    else:
        min_date = now + relativedelta(day=1)
        max_date = now + relativedelta(day=1, months=+1, days=-1)

    presenca = Presenca.objects.filter(datapresenca=datetime.today()).count()

    topT = Presenca.objects.values('nome').annotate(numeroatleta_count=Count('numeroatleta')).filter(
        datapresenca__gte=min_date,
        datapresenca__lte=max_date).order_by('-numeroatleta_count')[:20]

    try:
        novos = Atleta.objects.filter(created_at__month=now.month).count()
    except:
        pass

    novos = Atleta.objects.filter(created_at__month=now.month).count()
    qtmes = Presenca.objects.filter(created_at__month=now.month).count()

    context = {'presencas': presenca,
               'top': topT,
               'mes': qtmes,
               'novos': novos}

    return render(request, 'administration/index.html', context)
