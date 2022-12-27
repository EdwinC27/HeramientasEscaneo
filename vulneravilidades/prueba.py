import http.client

host = "localhost"
http = http.client.HTTPConection(host, timeout=2)
http.requets("HEAD", "")
server = http.getresponse().getheader('server')
vulnerables = open("vulnerables.txt", "r")
esVulnerable = False

for servicio in vulnerables:
	s = servicio.split(" ")
	if(s[0] in server):
		print(host,"tiene servicio", s[0],"con posible vulnerabilidad",s[1])
		esVulnerable = True
if(not esVulnerable):
	print(host,"no cuenta con un servicio vulnerable de la lista, o no da la informacion")


