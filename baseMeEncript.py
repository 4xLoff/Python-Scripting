#!/usr/bin/python3

import base64
import argparse

class Exploit:
    def __init__(self, input_base64, output_base64):
        self.input_base64 = input_base64
        self.output_base64 = output_base64
    
    def run(self):
        with open(self.input_base64, 'r') as archivo_entrada, open(self.output_base64, 'a') as archivo_salida:
            for linea in archivo_entrada:
                linea_codificada = base64.b64encode(linea.encode()).decode()
                archivo_salida.write(linea_codificada + '\n')

def get_arguments():
    parser = argparse.ArgumentParser(description='Usage: python3 tobase64.py <input_file_or_string> <output_file>')
    parser.add_argument('-i', '--input', dest='input_base64', required=True, help='Introduce una palabra o lista de palabras')
    parser.add_argument('-o', '--output', dest='output_base64', required=True, help='Proporcionar el nombre del fichero de salida')
    return parser.parse_args()

def main():
    args = get_arguments()
    exploit = Exploit(args.input_base64, args.output_base64)
    exploit.run()
    print("Encoding to Base64 completed.")

if __name__ == '__main__':
    main()
