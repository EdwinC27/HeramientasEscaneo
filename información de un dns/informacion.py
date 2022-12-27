# Obtenemos información de nuestro objetivo a través de su DNS

import dns.resolver
def main():
    try:
        objetivo = dns.resover.query("DNS","A")

        for x in objetivo:
            print(x)

    except:
        print("No pude obtener infrmacion")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

