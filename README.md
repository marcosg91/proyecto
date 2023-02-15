# proyecto
proyecto de pagina web ene/2023

metodo 1:
para correr el proyecto, hay que crear un archivo .env al mismo nivel del settings.py con la siguiente estructura: 

NAME=xxxxxx
USER=xxxxxx
PASSWORD=xxxxxx
HOST=DESKTOP-xxxxxx

metodo 2:
crear el archivo local.py al mismo nivel que base.py en settings (proyecto/proyecto/settings), con la siguiente estructura: 

############################################
from . base import *

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': "catalogo",
        'USER': "sa",
        'PASSWORD': "123",
        'HOST': "DESKTOP-B6JPFO0",
        'OPTIONS':{
            'driver': 'ODBC Driver 17 for SQL Server'
        },
    }
}
############################################
