from django.shortcuts import render
from django.views.decorators.cache import cache_page
from kettclub.assiduousness.forms import AssiduityForm


@cache_page(60)
def new(request):
    return render(request, 'assiduousness/assiduity_form.html',
                  {'form': AssiduityForm()})
