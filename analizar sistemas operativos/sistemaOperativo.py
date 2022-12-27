# Herramientas para Analizar sistemas operativos con Python

import os

print("Ubicacion archivo python: " + os.getcwd())
# getcwd() = encontrar la ubicacion del archivo

os.chdir("ruta")
# chdir() = modifica la ubicacion, pero no mueve el archivo

print("Ubicacion actual: " + os.getcwd())

print(os.listdir(os.getcwd()))
'''
listdir = te tra todos los archivos que estan en esta dirrecion: 
C:/Users/Edwin/Deskto
'''

