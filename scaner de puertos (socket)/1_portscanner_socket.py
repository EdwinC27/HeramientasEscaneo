import sys
import socket
from datetime import datetime

def main():
	target = "192.168.1.71" # ip del objetivo 

	print("-"*50)
	print("El target es : " + target)
	print("Inicio de escaneo: " +str(datetime.now()))
	print("-"*50)

# existen 65536 puertos, pero yo puse nomas que recorriera 80 
	for port in range(1,81): # recorrerer los puertos 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# AF_INET es para IPv4 
		socket.setdefaulttimeout(1) # cuanto tiempo dura la consulta 
		result = s.connect_ex((target,port)) 

		if result == 0: # Si esto se cumple el puerto se encuentra abierto 
			print("El puerto {} se encuentra abierto".format(port))
		s.close()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
