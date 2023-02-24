from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


@login_required
def plataforma(request):
    api='https://api.coingecko.com/api/v3/coins/markets?vs_currency=BRL&order=market_cap_desc&per_page=201&page=1&sparkline=false'
    raw_data= requests.get(api).json()
    return render(request, 'plataforma/plataforma.html',context={'datas':raw_data})

@login_required
def mercado(request):
    return render(request,'plataforma/mercado.html')
