import sys
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',
help="Ingresa una URL con la posible vulnerabilidad (e.g) https://webiste.com/?parameter=")
parser = parser.parse_args()

def main():
	file = open('payload_lfi.txt','r') # archivo con los payload 
	file = file.read().split("\n")
	agent = {'User-Agent':'Firefox'} # que navegador 

	if parser.target:
		print('Se iniciará la ejecución en => {}'.format(parser.target))
		print("-"*50)
		for payload in file:
			consulta = requests.get(url=parser.target+payload,headers=agent)
			if 'root' in consulta.text:
				print('-'*50)
				print("Probable LFI: {}".format(parser.target+payload))
			else:
				pass

	else:
		print("Especifica una URL vulnerable")

if __name__ == '__main__':
	try:
		main()
	except:
		sys.exit()