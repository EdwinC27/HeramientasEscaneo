import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', help = "Indica el sitio web \n(e.g https://ejemplo.com)")
parser = parser.parse_args()

def main():
	if parser.target:
		subprocess.run("wad -u" + parser.target + "> tecnologias.txt", shell=True) 
		# crear un archivo con las tecnologias
		file = open("tecnologias.txt",'r') # abrir el archivo creado
		tecnologias = file.read()
		tecnologias = tecnologias.split("[")
		tecnologias = tecnologias[1].split("]")
		tecnologias = tecnologias[0]
		tecnologias = tecnologias.split('{')

		for tecnologia in tecnologias: # poner ordena lo que va a mostrar 
			nuevo = tecnologia.replace('\n','')
			nuevo = nuevo.replace('            ','')
			nuevo = nuevo.replace('"','')
			nuevo = nuevo.split('}')
			nuevo = nuevo[0]
			nuevo = nuevo.replace(',','\n')
			print(nuevo)
			print("-"*50)
			
	else:
		print("Porfavor ingresa un sitio web")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
		