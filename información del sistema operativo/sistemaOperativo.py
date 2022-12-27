# Extraemos información del sistema operativo objetivo con python

from subprocess import check_output
import subprocess

sistema = check_output('systeminfo', stderr=subprocess.STDOUT)

registro = open('registro.txt', 'w+')
registro.write(sistema)

print("Confirmacion de informacion sustraida")
registro.close()


