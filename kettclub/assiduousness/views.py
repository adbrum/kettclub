from django.shortcuts import render
from kettclub.assiduousness.forms import AssiduityForm


def new(request):
    return render(request, 'assiduousness/assiduity_form.html',
                  {'form': AssiduityForm()})
