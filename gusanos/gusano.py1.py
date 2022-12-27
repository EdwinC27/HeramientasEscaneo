# Realizamos un gusano que se multiplica en el sistema operativo con Python

import shutil
import sys

def main():
	if len(sys.argv) == 2:
		for x in range(0,int(sys.argv[1])):
			shutil.copy(sys.argv[0],sys.argv[0]+str(x)+'.py')
	else:
		print("Debes especificar la cantidad de gusanos a reproducir")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()