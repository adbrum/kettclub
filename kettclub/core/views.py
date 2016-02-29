from django.shortcuts import render
from kettclub.subscriptions.forms import SubscriptionForm


def home(request):
    context = {'form': SubscriptionForm}
    return render(request, 'index.html', context)