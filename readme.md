uso como maquina viertual pipenv
para instalar todos los modulos necesarios hay que instalar pipenv con pip install pipenv
luego arracar la shell dentro de la carpeta del proyecto con pipenv shell y despues le damos a pipenv install para instalar todas las
dependencias
tambien hay que crear un archivo secret.py junto al settings.py del proyecto y darle darles la siguiente configuración:
SECRET_KEY = 'clavesecreta'
la puedes generar en la consola con 
python generador-clave.py

si trabajas con mysql tienes que agregar a el archivo secret.py
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'nombre de la base de dato',
'USER': 'nombre de usuario',
'PASSWORD': 'passwordp',
'HOST': 'localhost',
'PORT': '3306',
}
}

