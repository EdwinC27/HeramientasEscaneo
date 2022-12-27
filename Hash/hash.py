# Hash con python

import hashlib

def main():

	clave = raw_input("Ingresa la palabra a transformar en Hash: ")

	md5 = hashlib.md5(clave).hexdigest()
	print("Este es un Hash MD5: " + md5)

	sha1 = hashlib.sha1(clave).hexdigest()
	print("Este es un Hash SHA1: " + sha1)

	sha224 = hashlib.sha224(clave).hexdigest()
	print("Este es un Hash SHA224: " + sha224)

	sha256 = hashlib.sha256(clave).hexdigest()
	print("Este es un Hash SHA256: " + sha256)

	sha384 = hashlib.sha384(clave).hexdigest()
	print("Este es un Hash SHA384: " + sha384)

	sha512 = hashlib.sha512(clave).hexdigest()
	print("Este es un Hash SHA512: " + sha512)

if __name__ == '__main__':
	main()

