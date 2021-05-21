from setuptools import setup

setup(
    name="packs",
    version="1.0",
    description="Operaciones matematicas basicas",
    author="Eli",
    url="Eli.com",
    packages=["paquetes","paquetes.operacionesbasicas"]
    #rais, ruta
)

#python setup.py sdist 
#python3 setup.py sdist
#dirigir a la carpeta sdist e installar:
# pip3 install packs-1.0.tar.gz
#para desinstalar 
#pip3 unistall packs

