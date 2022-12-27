# Escaneamos los Temas de nuestro objetivo (ver si usa Divi (WordPress ) )

import requests
from bs4 import BeautifulSoup

def main():
	agente = {'User-Agent':'Google'}
	objetivo = requests.get(url="https://",headers=agente)
	parseamos = BeautifulSoup(objetivo.text,'html5lib')
	for link in parseamos.find_all('link'):
		if 'wp-content/themes/' in link.get('href'):
			tema = link.get('href')
			tema = tema.split('/')
			if 'themes' in tema:
				posicion = tema.index('themes')
				temas = tema[posicion+1]
				print("El tema que usa es: " + temas)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()


