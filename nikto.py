import os 
import sys
import re
import time
import linecache
import globalt
import vulnscans
from clear import clear
from logo import *

def start(): 
    with open('nikto/proxy.py') as f:
        global proxy
        proxy = f.read()
    with open('nikto/customArgs.py') as f:
        global customArgs
        customArgs = f.read()
        
    global target
    target = globalt.target
    clear()
    menu()
    

def menu():
    logo()
    global proxy
    global target
    global customArgs
    print("Current Target: [" + BC.F + target + BC.G + "]")
    print("Custom Arguments: [" + BC.F + customArgs + BC.G + "]")
    print("Current Proxy: [" + BC.F + proxy[11:] + BC.G + "]")
    global menuz
    mitems("Use A Proxy", "Clear Proxy", "Scan")
    mi = input("")
    '''
    for idx, i in enumerate(mitems, start=1):)
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "!" + BC.G + "] Vuln Scan Menu")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
        mi = input("")
    '''
    mp = mi[:7]
    mo = mi[8:]
    np = mi[:5]
    no = mi[6:]
    if mi == "1":
        clear()
        proxy = input("Enter Proxy: ")
        with open('nikto/proxy.py', 'w') as f:
            f.write(' -useproxy ' + proxy)            
        with open('nikto/proxy.py') as f:
            proxy = f.read()
        menu()
        #clear()
    elif mi == "2":
        clear()
        with open('nikto/proxy.py', 'w') as f:
            f.write("")
            proxy = ""
        menu()        
    elif mi == "3":
        clear()
        os.system('nikto -h ' + target + proxy)
        menu()
    elif mi == "!":
        vulnscans.menu()
    elif mi == "*":
        quit
    elif mi == "0":
        sys.exit()()
    elif mp == "!target":
        with open('globalt.py', 'w') as f:
            f.write('target = "' + mo + '"')
        globalt.target = mo
        target = mo
        clear()
        menu()
    elif mp == "#target":
        target = mo
        clear()
        menu()
    elif np == "#help":
        os.system( 'nikto --help' )
        input("Press Enter To Continue...")
        menu()
    elif np == "!help" or mi == "**":
        clear()
        helpm()
        input("Press Enter To Continue...")
        menu()
    elif np == "#args":
        with open('nikto/customArgs.py', 'w') as f:
            f.write(no)
        customArgs = no
        clear()
        menu()
    else:
        clear()
        print("WHELP! That didn't quite work...")
        time.sleep(1)
        menu()