from django.shortcuts import render
from .models import User
from .forms import FormDati
#from django.template import loader
#from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from hashlib import md5
#from django.urls import reverse

import random

def index(request):
	return render(request, 'chat/index.html')
   
def registration(request):
	return render(request, 'chat/registration.html')

def userlist(request):
	return render(request, 'chat/userlist.html')

def chat(request, nickname):
	#controllare che l'utente inserito esista nella tabella users
	#creare una tabella con gli id dei due utenti
	#pensare al meccanismo di salvataggio
	return render(request, 'chat/private_chat.html', { 'nickname' : nickname })


def adduser(request):
	if request.method == 'POST':

		form = FormDati(request.POST)

		if form.is_valid():

			dati = form.cleaned_data
			nickname = dati['nickname']
			password =  dati['password']

			if not (User.objects.filter(nickname = nickname).exists()):
				
				user = User(
					nickname = nickname,
					password = md5(password.encode()).hexdigest(),
					color = '%06x' % random.randint(0, 0xFFFFFF)
				)

				user.save()
				
				return HttpResponseRedirect('../')
			else:
				return HttpResponseRedirect('/reg/')
	else:
		return HttpResponseRedirect('/reg/')

def logging(request):
	#da mettere a posto
	if request.method == 'POST':

		form = FormDati(request.POST)

		if form.is_valid():

			dati = form.cleaned_data
			nickname = dati['nickname']
			password =  dati['password']

			print(nickname)
			print(password)

			if (User.objects.filter(nickname = nickname).exists() and User.objects.filter(password = password).exists()):
				#utente loggato
				return HttpResponseRedirect('/list/')
			else:
				return HttpResponseRedirect('../')
	else:
		return HttpResponseRedirect('../')