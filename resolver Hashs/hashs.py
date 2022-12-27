# Rompemos Hash (contraseñas) con Python. Ataques de fuerza bruta

import hashlib

def main():
	resolverhash = raw_input("Ingrese el Hash a resolver: ")
	resolvedor = open("resolvedordeclaves.txt",'r')

	for x in resolvedor.readlines():
		a = x.strip("\n")
		a = hashlib.sha1(a).hexdigest()
		if a == resolverhash:
			print("Clave:  {}El hash resuelto:   {}".format(x,a))

if __name__ == '__main__':
	main()
