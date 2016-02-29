from django.shortcuts import render
from kettclub.subscriptions.forms import SubscriptionForm


def new(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})
