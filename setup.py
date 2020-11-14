#Configuración del paquete distribuible
from setuptools import setup

setup(
    #atributos necesarios para la creación de un paquete distribuible
    name="paquete_calculos",
    version="1.0",
    description="Paquete de redondeo y potencia",
    author="César",
    author_email="cjaureguisaavedra@gmail.com",
    url="",
    packages=["calculos","calculos.redondeo_potencia"]
)

'''
Luego se tiene que instalar el paquete en el sistema operativo con el siguiente comando en la terminal (todo esto en el directorio raíz del proyecto):

    python setup.py sdist

Después nos dirigimos a la carpeta dist que se acaba de crear:

    cd dist

Instalamos el paquete en el sistema operativo

    pip3 install paquete_calculos-1.0.tar.gz

Nota: si sale la siguiente advertencia 

    "WARNING: You are using pip version 19.2.3, however version 20.2.4 is available.
    You should consider upgrading via the 'python -m pip install --upgrade pip' command."

Es porque el pip de windows está desactualizado. Se debe poner el siguiente comando y luego probar instalar el paquete de nuevo:

    python -m pip install --upgrade pip

Para desinstalar el paquete ponemos el siguiente comando

    pip3 uninstall paquete_calculos

'''