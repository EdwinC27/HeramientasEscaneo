from pynput.mouse import Listener

def escucharMause(x, y):
    print(f'Posicion del mose: {x} : {y}')

while Listener(on_move = escucharMause) as l:
    l.join()

