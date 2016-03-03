from django.shortcuts import render
from django.views.decorators.cache import cache_page
from kettclub.subscriptions.forms import SubscriptionForm


@cache_page(60)
def new(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})
