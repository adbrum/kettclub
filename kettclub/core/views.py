from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from kettclub.core.form import EmailForm, SubscriptionForm


class Email(object):
    pass


# def home(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#
#             body = render_to_string('email.txt',form.cleaned_data)
#             mail.send_mail('Solicitação de serviços',
#                            body,
#                            'adbrumvidal@gmail.com',
#                            ['adbrumvidal@gmail.com', form.cleaned_data['email']])
#             email = Email.objects.create(**form.cleaned_data)
#
#             messages.success(request, 'Solicitação enviada com sucesso!')
#
#             return HttpResponseRedirect('/')
#         else:
#             return render(request, 'index.html', {'form': form})
#
#     else:
#         context = {'form': EmailForm}
#         return render(request, 'index.html', context)
def home(request):
    context = {'form': SubscriptionForm}
    return render(request, 'index.html', context)