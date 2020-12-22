import os 
import sys
import re
import time
import nmap
import masscan
import cms
import ipgeo
import nikto
import linecache
from clear import clear
from logo import *


#### Add custom args to nmap
def menu():
    clear()
    logo()
    mi = print("Vuln Scanners")
    """Social Engineering Tool Kit"""
    mitems = ("Nmap", "Nikto", "Masscan", "IPGeoLocation", "CMS Scanners")
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
        mi = input("")
    mp = mi[:7]
    mo = mi[8:]
    np = mi[:5]
    no = mi[6:]
    if mi == "1":
        nmap.start()
        clear()
    elif mi == "2":
        nikto.start()
        clear()
    elif mi == "3":
        masscan.start()
        clear()
    elif mi == "4":
        ipgeo.start()
        clear()
    elif mi == "5":
        clear()
        cms.start()
    elif mi == "*":
        clear()
        quit
    elif mi == "0":
        sys.exit()()
    elif mp == "!target":
        with open('globalt.py', 'w') as f:
            f.write('target = "' + mo + '"')
        globalt.target = mo
        target = mo
        menu()
    elif np == "!help" or mi == "**":
        clear()
        helpm()
        input("Press Enter To Continue...")
        menu()
    else:
        clear()
        print("WHELP! That didn't quite work...")
        time.sleep(1)
        menu()