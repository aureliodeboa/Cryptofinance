from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
def envia_email(request):
    #send_mail('Troca de senha', 'link','naorespondacryptofinance@outlook.com',['aurelio74123@gmail.com'])
    return HttpResponse('PLATAFOMRA')
