from django.shortcuts import render
from django.views.decorators.cache import cache_page
from kettclub.subscriptions.forms import SubscriptionForm


@cache_page(60)
def home(request):
    context = {'form': SubscriptionForm}
    return render(request, 'index.html', context)
