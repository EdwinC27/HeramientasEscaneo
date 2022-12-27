# Ver en que servidor está la página y que paginas en ese mismo servidor

import requests
from bs4 import BeautifulSoup

def main():
    objetivo = "achirou.com" # dirrecion de la pagina
    agente = {'User-Agent':'Google'} # donde lo va a buscar
    web = requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(objetivo), headers=agente)
    # busca
    bea = BeautifulSoup(web.text, 'html5lib')
    buscar = bea.find(id="null")
    siteos = buscar.find(border="1")

    for x in siteos.find_all("tr"): # tr te lo muestra como una tabla
        print("Siteos: "+x.td.string)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()

