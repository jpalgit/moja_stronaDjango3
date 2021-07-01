from django.shortcuts import render
from django.http import HttpResponse
from . forms import Kwanty
import math
import json
# Create your views here.


def termodynamika(request):
    formularz = Kwanty
    if request.method == "POST":
        formularz = Kwanty(request.POST)
        if formularz.is_valid():
            dane = formularz.cleaned_data
            atomy = dane['atomy']
            kwanty = dane['kwanty']
            wynik = math.factorial(atomy-1+kwanty)/(math.factorial(atomy-1)*math.factorial(kwanty))
            return HttpResponse(json.dumps({'wyniki': wynik}), content_type='application/json')

    # return render(request, 'fizyka/termodynamika.html', {'formularz': formularz})
    return render(request, 'fizyka/term.html', {'formularz': formularz})