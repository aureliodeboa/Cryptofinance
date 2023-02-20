
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from portifolio.models import Carteira

import requests

def carteira(request):
    if request.method=='POST':
        nome_moeda= request.POST.get('nome_moeda')
        simbolo_moeda= request.POST.get('simbolo_moeda')
        quantidade_moeda= request.POST.get('quantidade_moeda')
        if nome_moeda:
            Carteira.objects.create(usuario=request.user,moeda=nome_moeda,symbol=simbolo_moeda, quantidade=quantidade_moeda)
            print('TUDO SALVO MEU LINDO!!')
            return HttpResponseRedirect(reverse('carteira'))

    else:
        #https://api.coingecko.com/api/v3/coins/NAME
        carteira_objs= Carteira.objects.filter(usuario=request.user)
        nome_moeda_list=[]
        preco_moeda_list=[]

        for obj in carteira_objs:
            coin_api= f'https://api.coingecko.com/api/v3/coins/{obj.moeda}' #o nome que ta escrito no models
            raw_data_single= requests.get(coin_api).json()
            #print(raw_data_single)
            float_quantidade= float(obj.quantidade)
            preco_atual= raw_data_single['market_data']['current_price']['brl']
            preco_total= float_quantidade * preco_atual
            nome_moeda_list.append(obj.moeda)
            preco_moeda_list.append(preco_total)

        final_list= zip(nome_moeda_list, preco_moeda_list)
        data={
            'dataList':final_list
        }

        return render(request, 'carteira/carteira.html',context=data)

