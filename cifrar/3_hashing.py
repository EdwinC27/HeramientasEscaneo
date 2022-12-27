import hashlib
import sys

def md5(palabra):
	encrypted = hashlib.md5(palabra)
	print(encrypted.hexdigest())

def sha1(palabra):
	encrypted = hashlib.sha1(palabra)
	print(encrypted.hexdigest())

def sha256(palabra):
	encrypted = hashlib.sha256(palabra)
	print(encrypted.hexdigest())

def sha512(palabra):
	encrypted = hashlib.sha512(palabra)
	print(encrypted.hexdigest())

def main():
	print(".:CIFRADOR:.")
	print("Elige el metodo de ciframiento")
	print("1.MD5\n2.SHA1\n3.SHA256\n4.SHA512\n#.Salir")
	modo = int(input("=> "))
	palabra = "hola" # palabra a cibfrar para comparar
	palabra = palabra.encode('utf-8')
	print("-"*20)

	if modo == 1:
		md5(palabra)
	elif modo == 2:
		sha1(palabra)
	elif modo == 3:
		sha256(palabra)
	elif modo == 4:
		sha512(palabra)
	else:
		sys.exit()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
