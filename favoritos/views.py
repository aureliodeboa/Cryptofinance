from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from favoritos.models import Favoritos
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
@login_required
def favoritos(request):
    if request.method=='POST':
        nome_moeda= request.POST.get('nome_moeda')
        if nome_moeda:
            coin_api= f'https://api.coingecko.com/api/v3/coins/{nome_moeda}' #verificar se o nome digitado esta certo
            nome= requests.get(coin_api).json()
            try:
                if(nome['error']=='coin not found'):
                    messages.warning(request,'Nome incorreto, tente novamente!!')
                    return HttpResponseRedirect(reverse('favoritos'))
            except:
                Favoritos.objects.create(usuario=request.user,moeda=nome_moeda)
                print('TUDO SALVO MEU LINDO!!')
                return HttpResponseRedirect(reverse('favoritos'))
                
        

    else:
        #https://api.coingecko.com/api/v3/coins/NAME
        favoritos_objs= Favoritos.objects.filter(usuario=request.user)
        nome_moeda_list=[]
        id_list=[]
        for obj in favoritos_objs:
            nome_moeda_list.append(obj.moeda)
            id_list.append(obj.id)


        final_list=zip(nome_moeda_list,id_list)
        data={
    
            'dataList':final_list,
        }

        return render(request, 'favoritos/favoritos.html',context=data)


def apagar(request,id):
    instance=get_object_or_404(Favoritos,id=id)
    instance.delete()
    
    #Carteira.objects.filter(id=id).delete()

    return HttpResponseRedirect(reverse('favoritos'))
