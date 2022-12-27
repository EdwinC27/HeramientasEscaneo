import hashlib
import sys

def md5(palabra,lista):
	lista = lista.split('\n')
	for i in lista:
		cifrado = i.encode('utf-8')
		encrypted = hashlib.md5(cifrado)
		if palabra == encrypted.hexdigest():
			print("(+) Se descifro la palabra: {}".format(i))
			break
		else:
			pass

def sha1(palabra,lista):
	lista = lista.split('\n')
	for i in lista:
		cifrado = i.encode('utf-8')
		encrypted = hashlib.sha1(cifrado)
		if palabra == encrypted.hexdigest():
			print("(+) Se descifro la palabra: {}".format(i))
		else:
			pass

def sha256(palabra,lista):
	lista = lista.split('\n')
	for i in lista:
		cifrado = i.encode('utf-8')
		encrypted = hashlib.sha256(cifrado)
		if palabra == encrypted.hexdigest():
			print("(+) Se descifro la palabra: {}".format(i))
		else:
			break

def sha512(palabra,lista):
	lista = lista.split('\n')
	for i in lista:
		cifrado = i.encode('utf-8')
		encrypted = hashlib.sha512(cifrado)
		if palabra == encrypted.hexdigest():
			print("(+) Se descifro la palabra: {}".format(i))
			break
		else:
			pass

def main():
	print(".:WELCOME TO PASSWORD GUESSER:.")
	print("Este programa solo descifra MD5 - SHA1 - SHA256 - SHA512")
	palabra = input("Ingresa el hash a descifrar: ")

	file = open("contrasenas.txt",'r')
	lista = file.read()

	print("(+) Identificando el metodo de ciframiento")
	if len(palabra) == 32:
		print("(+) El hash se encuentra cifrado en MD5")
		md5(palabra,lista)

	elif len(palabra) == 40:
		print("(+) El hash se encuentra cifrado en SHA1")
		sha1(palabra,lista)

	elif len(palabra) == 64:
		print("(+) El hash se encuentra cifrado en SHA256")
		sha256(palabra,lista)

	elif len(palabra) == 128:
		print("(+) El hash se encuentra cifrado en SHA512")
		sha512(palabra,lista)
		
	else:
		print("(-) No contamos con ese metodo de desciframiento")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
