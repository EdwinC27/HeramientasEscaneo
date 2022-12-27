# Realizamos búsquedas específicas en google con mechanize y web scraping (para sacar la información de alguien).

import mechanize
import argparse
from bs4 import BeautifulSoup

argparser = argparse.ArgumentParser()
argparser.add_argument("-b", '--buscar', help="Opcion a buscar")
#                       -b es la palabra es una obrebiatura de buscar
argparser = argparser.parse_args()


def main():
    if argparser.buscar:
        search = mechanize.Browser()
        search.set_handle_robots(False)
        search.set_handle_equiv(False)
        search.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0')]
        search.open("https://www.google.com")

        search.select_form(nr=0)
        search['q'] = argparser.buscar
        search.submit()
        b = BeautifulSoup(search.response().read(), 'html5lib')
        for x in b.find_all('a'):
            l = x.get('href')
            l = l.replace('/url?q=', '')
            print(l)

    else:
        print("Palabra que queremos buscar")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()

