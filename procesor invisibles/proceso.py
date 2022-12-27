# Creamos procesos sin que sepa el usuario con python

import subprocess
import os

esconder = open(os.devnull,"w")

proceso = subprocess.call(['ping', '8.8.8.8'], stdout=esconder, stderr=subprocess.STDOUT)
# '8.8.8.8' es la DNS IPv4 de google

if proceso == 0:
    print("El proceso se escondio con exito")
else:
    print("Algo salio mal")


# os.system("ping 8.8.8.8")