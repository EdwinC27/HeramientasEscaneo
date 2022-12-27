# Escaneamos los Usuarios de nuestro objetivo

import json
import urllib.request

def main():
	objetivo = urllib.request.urlopen("https://")
										# url del siteo
	for x in json.loads(objetivo.read()):
		usuario = x['slug']
	print(usuario)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()

