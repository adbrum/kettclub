from django.shortcuts import render
from kettclub.reviewsphysicals.forms import EvaluationForm


def new(request):
    return render(request, 'reviewsphysicals/evaluation_form.html',
                  {'form': EvaluationForm()})
