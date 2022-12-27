import os
import sys
import time

def switcher(opcion):
	if opcion == 1: #SCAN COMPLETO
		nmap_cadena = " -p- -A"
		return nmap_cadena

	elif opcion == 2: #SCAN LIGHT
		nmap_cadena = " -T5 --top-ports 10"
		return nmap_cadena

	elif opcion == 3: #SCAN HOST DISCOVERY
		nmap_query = " -sn"
		return nmap_query

	elif opcion == 4: #SCAN VULN
		nmap_query = " --script vuln"
		return nmap_query

	elif opcion == 5: # SCAN OS
		nmap_query = " -O"
		return nmap_query


	elif opcion == 6: # SCAN VERSION
		nmap_query = " -sV"
		return nmap_query

	else:
		sys.exit()

def parser(modo,nmap_query,ip):
	if modo == 2:
		print("-"*50)
		print(ip)
		results = os.popen(nmap_query).read()
		results = results.split("latency).\n\n")
		results = results[1].split("MAC Address")
		results = results[0]
		print(results)
	elif modo == 3:
		print("-"*50)
		print(ip)
		results = os.popen(nmap_query).read()
		results = results.split("address (")
		results = results[1].split(" ho")
		results = results[0]
		if results == "1":
			print("El host se encuentra encendido")
		else:
			print("El host se encuentra apagado")
	else:
		print("-"*50)
		print(ip)
		results = os.system(nmap_query)

def option(opcion,mode,modo):
	if opcion == 1:
		print("Indique la IPv4 (e.g 192.168.1.1)")
		target = "192.168.1.72"#input("=> ")
		consulta = "nmap " + target + mode
		parser(modo,consulta,target)

	else:
		print("Indica el nombre del archivo de texto (e.g archivo.txt)")
		archivo = "ipv4.txt"#input("=> ")
		file = open(archivo,'r')
		ips = file.read().split("\n")
		for ip in ips:
			consulta = "nmap " + ip + mode
			parser(modo,consulta,ip)

def main():
	print("Bienvenidos a NMAP automatizado...")
	time.sleep(1)
	print("Elige un modo de ejecucion")
	print("[1]. Scan Completo\n[2]. Scan Light\n[3]. Host Discovery\n[4]. Scan Vuln\n[5]. Scan OS\n[6]. Scan Version\n[#].Salir")
	modo = 3#int(input("=> "))
	mode = switcher(modo)
	time.sleep(1)
	print("-"*50)
	print("Elige una opcion\n[1]. IPv4\n[#]. Lista")
	opcion = 2#int(input("=> "))
	option(opcion,mode,modo)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Finalizando...")
		sys.exit()