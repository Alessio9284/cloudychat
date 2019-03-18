# Progetto di Alessio Torricelli

## CHAT PRIVATE

- Django (Framework Python)
- SQLite3 (Database)
- Heroku (Web Hosting e altro)
- Lato Client:
  - HTML, CSS, JS
  - Richieste AJAX


## CONFIGURAZIONE DATABASE

	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}


## INSTALLAZIONE

- pip install -r requirements.txt
- python manage.py migrate
- python manage.py makemigrations
- python manage.py runserver