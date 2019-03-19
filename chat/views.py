from django.shortcuts import render
from .models import User, Message
from .functions import FormDati
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from hashlib import md5
from django.core import serializers
from django.db.models import Q

import random
import json

def index(request):

	if 'nickname' in request.session and 'password' in request.session and 'color' in request.session:
		
		nickname = request.session['nickname']
		password = request.session['password']

		# Utente inattivo
		User.objects.filter(nickname = nickname, password = password).update(active = False)

	# Distruzione della sessione
	for k in list(request.session.keys()):
		del request.session[k]

	return render(request, 'chat/index.html')
   
def registration(request):
	return render(request, 'chat/registration.html')

def userlist(request):

	checkSession(request)

	nickname = request.session['nickname']
	password = request.session['password']

	# Utente attivo
	User.objects.filter(nickname = nickname, password = password).update(active = True)

	return render(request, 'chat/userlist.html')

def chat(request, nickname):

	checkSession(request)

	if User.objects.filter(nickname = nickname, active = True).exists():

		frm = request.session['nickname']

		return render(request, 'chat/private_chat.html', {'to' : nickname, 'frm' : frm})

	return HttpResponseRedirect('../')

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

def updatelist(request):

	checkSession(request)

	userlist = serializers.serialize('json', User.objects.filter(active = True))

	return JsonResponse(userlist, safe = False)


def updatemessages(request, nickname):

	checkSession(request)

	if int(request.POST['messages']) != Message.objects.all().count():

		frm = request.session['nickname']

		if frm == nickname:
			messages = serializers.serialize('json',
				Message.objects.filter(frm = frm, to = nickname).order_by('id')
			)
		else:
			messages = serializers.serialize('json', 
				Message.objects.filter(Q(frm = frm, to = nickname) | Q(frm = nickname, to = frm)).order_by('id')
			)

		return JsonResponse(messages, safe = False)

	return JsonResponse("nochange", safe = False)

def addmessage(request):

	checkSession(request)

	if request.method == 'POST':

		frm = request.session['nickname']
		to = request.POST['to']

		# Creazione del messaggio tramite un oggetto
		message = Message(
			text = request.POST['message'],
			date = request.POST['date'],
			frm = User.objects.get(nickname = frm),
			to = User.objects.get(nickname = to),
		)

		# INSERT nel database
		message.save()

	return JsonResponse("add", safe = False)

def truncate(request):

	# Eliminazione di tutti i record nei modelli
	User.objects.all().delete()
	Message.objects.all().delete()

	return HttpResponseRedirect('../')

# FUNCTIONS

def checkSession(r):
	if 'nickname' not in r.session or 'password' not in r.session or 'color' not in r.session:

		return HttpResponseRedirect('../')