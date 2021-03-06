import os 
import sys
import re
import time
import linecache
import vulnscans
from clear import clear
from logo import *

def start():    
    with open('nmap/customArgs.py') as f:
        global customArgs
        customArgs = f.read()
        global target
    target = globalt.target
    clear()
    menu()
    

def menu():
    logo()
    global customArgs
    global target
    mi = print("Current Target: [" + BC.F + target + BC.G + "]")
    mi = print("Custom Arguments: [" + BC.F + customArgs + BC.G + "]")
    mitems("Quick Port Scan", "Deep Port Scan", "System Info Scan", "Known Vuln Scan", "Run With Just Custom Arguments")
    mi = input("")
    mp = mi[:7]
    mo = mi[8:]
    np = mi[:5]
    no = mi[6:]
    na = mi[6:]
    if mi == "1":
        clear()
        os.system('nmap --top-ports 20 %s %s ' % (target, customArgs))
        menu()
        #clear()
    elif mi == "2":
        clear()
        os.system('sudo nmap -v -sS -sV %s %s ' % (target, customArgs))
        menu()
    elif mi == "3":
        clear()
        os.system('sudo nmap -O %s %s ' % (target, customArgs))
        menu()
    elif mi == "4":
        clear()
        os.system('nmap -Pn --script vuln %s %s ' % (target, customArgs))
        menu()
    elif mi == "5":
        clear()
        os.system('sudo nmap %s %s ' % (target, customArgs))
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
        os.system( sqlmapdir + ' -h' )
        menu()
    elif np == "!help" or mi == "**":
        clear()
        helpm()
        menu()
    elif np == "#args":
        with open('nmap/customArgs.py', 'w') as f:
            f.write(no)
        customArgs = no
        clear()
        menu()
    elif np == "#port":
        ports = no
        clear()
        menu()
    else:
        clear()
        print("WHELP! That didn't quite work...")
        time.sleep(1)
        menu()
        