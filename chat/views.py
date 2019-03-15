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

	# Distruzione della sessione
	for k in list(request.session.keys()):
		del request.session[k]

	return render(request, 'chat/index.html')
   
def registration(request):
	return render(request, 'chat/registration.html')

def userlist(request):

	if 'nickname' not in request.session or 'password' not in request.session or 'color' not in request.session:

		return HttpResponseRedirect('../')

	return render(request, 'chat/userlist.html')

def chat(request, nickname):

	if 'nickname' not in request.session or 'password' not in request.session or 'color' not in request.session:

		return HttpResponseRedirect('../../')

	return render(request, 'chat/private_chat.html', { 'nickname' : nickname })


def adduser(request):

	if request.method == 'POST':

		# Prendo i dati del Form
		form = FormDati(request.POST)

		# Controllo che il form sia valido
		if form.is_valid():

			# Raccolgo i dati in modo da essere utilizzabili
			dati = form.cleaned_data
			nickname = dati['nickname']

			# Controllo che il nome utente non esista già
			if not (User.objects.filter(nickname = nickname).exists()):

				password =  dati['password']
				
				# Creazione dell'utente tramite un oggetto
				user = User(
					nickname = nickname,
					password = md5(password.encode()).hexdigest(),
					color = '%06x' % random.randint(0, 0xFFFFFF)
				)

				# INSERT nel database
				user.save()
				
				return HttpResponseRedirect('../')
			
			return HttpResponseRedirect('/reg/')
	
	return HttpResponseRedirect('/reg/')

def logging(request):

	if request.method == 'POST':

		# Prendo i dati del Form
		form = FormDati(request.POST)

		# Controllo che il form sia valido
		if form.is_valid():

			# Raccolgo i dati in modo da essere utilizzabili
			dati = form.cleaned_data

			nickname = dati['nickname']
			password = md5(dati['password'].encode()).hexdigest()

			# Controllo se l'utente esiste
			user = User.objects.filter(nickname = nickname, password = password)

			if (user.exists()):

				# Estrazione del colore dall'utente salvato
				color = User.objects.get(nickname = nickname, password = password).color

				request.session['nickname'] = nickname
				request.session['password'] = password
				request.session['color'] = color

				return HttpResponseRedirect('/list/')

			return HttpResponseRedirect('../')

	return HttpResponseRedirect('../')