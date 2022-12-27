import requests
import argparse

parser = argparse.ArgumentParser(description="Detector de web")
parser.add_argument('-t', '--target', help="objetivo")
parser = parser.parse_args()

def main():
    if parser.target:
        try:
            url = requests.get(url=parser.target)
            web = dict(url.headers)

            for x in web:
                print(x + " : " +web[x])

        except:
            print("No se logro llegar al objetivo")
    else:
        print("No se encuentra el objetivo")

if __name__ == "__main__":
    main()


