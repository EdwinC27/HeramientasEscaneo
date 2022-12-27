import dns.resolver

def main():
    informacion = ['A', 'AAAA', 'NS', 'SOA', 'MX', 'MF', 'MD', 'TXT']

    for x in informacion:
        try:
            direccion = dns.resolver.query("DNS.com", x)
            # dirrecion a investigar
            for y in direccion:
                print(y)
        except:
            print("No se pouede encontrar la consulta")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
