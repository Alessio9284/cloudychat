from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html')
   
def registration(request):
    return render(request, 'registration.html')

def userlist(request):
    return render(request, 'userlist.html')

def chat(request, nickname):
    #controllare che l'utente inserito esista nella tabella users
    #creare una tabella con gli id dei due utenti
    #pensare al meccanismo di salvataggio
    return render(request, 'private_chat.html', { 'nickname' : nickname })
