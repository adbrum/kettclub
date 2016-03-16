from django.shortcuts import render
from django.views.decorators.cache import cache_page
from kettclub.subscriptions.forms import SubscriptionForm


@cache_page(60)
def home(request):
    context = {'form': SubscriptionForm}
    return render(request, 'index.html', context)


# # @cache_page(60)
# def dashboard(request):
#
#     # dmin = request.POST.get('date1')
#     # dmax = request.POST.get('date2')
#     min_date = datetime.strptime('01/03/2016', "%d/%m/%Y")
#     max_date = datetime.strptime('15/03/2016', "%d/%m/%Y")
#     top20 = Presenca.objects.annotate(Count('numeroatleta')).filter(datapresenca__gte=min_date, datapresenca__lte=max_date).order_by('-numeroatleta__count')[:20]
#     presenca = Presenca.objects.filter(datapresenca=datetime.today()).count()
#
#     # presenca = Presenca.objects.filter(datapresenca__gte=min_date, datapresenca__lte=max_date).count()
#
#     top = []
#     nomealuno = []
#
#     xxx = {}
#
#     print('TOP 200000000000: ')
#
#     for i in top20:
#         print('TOP 20: ', i.numeroatleta)
#         top.append(i.numeroatleta)
#
#
#     for i in nomealuno:
#         print(i)
#
#     top20 = list(set(top))
#     print('000000000000000: ', top20)
#
#
#     # s = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut"
#     c = collections.Counter(top)
#     print('COMUM', c.most_common(20))
#
#     revDct = dict((key, val) for (key, val) in c.most_common(20))
#
#     print('VVVVVVVVVVVVVVV; ', revDct)
#
#     changedDict = {}
#
#     for key, elem in revDct.items():
#         chave = Atleta.objects.get(pk=key)
#
#         changedDict.update(dict((chave.nome, elem) for (key, value) in revDct.items()))
#
#         print('DDDDDDDDDDDDDD', changedDict)
#
#     # changedDict = sorted(changedDict.values())
#
#     print('WWWWWWWWWWWWWWWWWWWWW', changedDict)
#
#         # revDct['ddd'] = revDct.pop(1)
#         # dic.rename(key,chave.nome)
#
#         # revDct[key] = chave.nome
#         # print(key, elem)
#
#     print('DICT: ', revDct)
#
#     atleta = Atleta.objects.filter(pk__in=top20)
#
#     # top20 = zip(*sorted(enumerate(atleta), key=operator.itemgetter(1)))[0][-2:]
#
#     for i in atleta:
#         print('ATLETA', i.nome)
#         nomealuno.append(i.nome)
#
#     context = {'presencas': presenca,
#                'top': top20,
#                'atletas': atleta,
#                'alunos': nomealuno,
#                'chan': changedDict}
#
#     return render(request, 'dashboard.html', context)
