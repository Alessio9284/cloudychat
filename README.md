# Progetto di Alessio Torricelli

## CHAT PRIVATE

- memorizzazione delle chat
- memorizzazione degli utenti tramite registrazione semplice
- lato client html, css, js (ajax)
- lato server python

## CONFIGURAZIONE DATABASE

	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql', 
			'NAME': 'heroku_e3f89a5afdbe8e0',
			'USER': 'bf199d2688f63a',
			'PASSWORD': '8296016b',
			'HOST': 'eu-cdbr-west-02.cleardb.net',
			'PORT': '',
			'OPTIONS': {
				'ssl': {
					'ca': 'certificates/cleardb-ca.pem',
					'cert': 'certificates/bf199d2688f63a-cert.pem',
					'key': 'certificates/bf199d2688f63a-key.pem'
				}
			}
		}
	}
