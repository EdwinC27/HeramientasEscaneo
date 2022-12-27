from pynput.keyboard import Controller
import sys

def controlTeclado():
    teclado = Controller()  
    teclado.type('Prueba de teclado')
    # aqui es lo que te escribe 

def main():
    controlTeclado()

if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit()
