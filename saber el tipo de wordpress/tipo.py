import requests
from bs4 import BeautifulSoup

def main():
	url = "https://" # dirrecion de la pagina
	cabecera = {'User-Agent':'Firefox'}
	peticion = requests.get(url=url,headers=cabecera)
	soup = BeautifulSoup(peticion.text,'html5lib')

	for v in soup.find_all('meta'):
		if v.get('name') == 'generator':
			version = v.get('content')
	print("El wordpress es: " + version)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo")
		exit()

