from pynput.mouse import Controller
import sys

def controlMause():
    mause = Controller()  
    mause.position = (200, 500)
    # aqui es la posicion

def main():
    controlMause()

if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit()

