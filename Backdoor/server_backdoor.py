import socket
import sys
import os

def main():
    ip = "0.0.0.0"
    port = 7890
    conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    conexion.bind((ip, port))
    conexion.listen(1)
    conn, addr = conexion.accept()
    print('[+] Conexion ', addr)

    while True:
        command = input("=> ")
        if command == 'exit':
            conn.send(b'exit')
            conn.close()
            break
            
        elif command == "":
            continue

        else:
            command = command.encode()
            conn.send(command)
            output = conn.recv(1024)
            print(output.decode('latin1'))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
