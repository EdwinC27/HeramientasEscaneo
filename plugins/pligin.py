#Escaneamos los Usuarios de nuestro objetivo

import requests
from os import path
from progress.bar import Bar

def main():
	if path.exists("wp_plugins.txt"):
		plugins = open("wp_plugins.txt", "r")
		plugins = plugins.read().split('\n')
		lista = []
		objetivo = "https://" # url de la pagina
		barra = Bar("Procesando...",max=len(plugins))

		for plugin in plugins:
			barra.next()
			try:
				plu = requests.get(url=objetivo+"/"+plugin)
				if plu.status_code == 200:
					resultado = objetivo+""+plugin
					lista.append(resultado.split("")[-2])
			except:
				pass
		barra.finish()
		for plugin in lista:
			print("Plugins: {}".format(plugin))
	else:
		print("No se encontro la lista")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()