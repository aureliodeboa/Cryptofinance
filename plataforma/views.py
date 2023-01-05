from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def plataforma(request):
    return render(request, 'plataforma/plataforma.html')