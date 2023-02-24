from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from favoritos.models import Favoritos
from django.contrib.auth.decorators import login_required

import requests
@login_required
def favoritos(request):
    if request.method=='POST':
        nome_moeda= request.POST.get('nome_moeda')
    
        if nome_moeda:
            Favoritos.objects.create(usuario=request.user,moeda=nome_moeda)
            print('TUDO SALVO MEU LINDO favoritos!')
            return HttpResponseRedirect(reverse('favoritos'))

    else:
        #https://api.coingecko.com/api/v3/coins/NAME
        favoritos_objs= Favoritos.objects.filter(usuario=request.user)
        nome_moeda_list=[]
       
        for obj in favoritos_objs:
            nome_moeda_list.append(obj.moeda)
            

        data={
            'dataList':nome_moeda_list,
            
        }

        return render(request, 'favoritos/favoritos.html',context=data)
