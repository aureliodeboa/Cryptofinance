from django.http import HttpResponse
from django.shortcuts import render

def inicial(request):
    #return HttpResponse('PAGINA INICIAL')
    return render(request, 'inicial.html')