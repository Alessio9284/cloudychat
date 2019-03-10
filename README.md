# Progetto di Alessio Torricelli

## CHAT PRIVATE

- memorizzazione delle chat
- memorizzazione degli utenti tramite registrazione semplice
- lato client html, css, js (ajax)
- lato server python, mysql


## MODULI

- sudo apt-get install python3-pymysql

## MYSQL

- sudo apt-get install mysql-server

## MYSQL WORKBENCH

- https://dev.mysql.com/downloads/workbench/

## CONFIGURAZIONE DATABASE

    DATABASES = {
        'default': {
          'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'django',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '33066',
        }
    }
