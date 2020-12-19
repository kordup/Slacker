#!/usr/bin/python3

import os 
from clear import clear
from logo import *
import time
import sqlmap
import hashc
import vulnscans
import cms
import dos
import dir
import re
from subprocess import call
import linecache
import metasploit

        
### TODO: 
######### Tools To Add: HashCat, Dir Tools, Admin Finder, FPing, IPGeolocation
######### Add Dir Tools, Admin Finder
######### Add Comments
######### Add SE Tool Kit


### Main Menu(s) ###
def Menus(a):
    if a == 1:
        logo()
        print("What type of trouble are we looking for?")
        mitems = ("Vulnerability Scans", "Hash Cracking", "DoS", "CMS Vuln Scans", "SQLMap", "Metasploit")
        for idx, i in enumerate(mitems, start=1):
            print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
        else:
            print("------------------------------------------")
            print(" [" + BC.F + "**" + BC.G + "] Help")
            print(" [" + BC.F + "0" + BC.G + "] Exit")
            mi = input("")
        mp = mi[:7]
        mo = mi[8:]
        np = mi[:5]
        no = mi[6:]
        if mi == "1":
            Menus(2)
        elif mi == "2":
            Menus(3)
        elif mi == "3":
            Menus(4)
        elif mi == "4":
            Menus(5)
        elif mi == "5":
            Menus(6)
        elif mi == "6":
            Menus(7)
        elif mi == "7":
            Menus(8)
        elif mi == "8":
            Menus(9)
        elif mi == "0":
            quit
        elif mp == "!target":
            with open('globalt.py', 'w') as f:
                f.write('target = "' + mo + '"')
            globalt.target = mo
            target = mo
            Menus(1)
        elif np == "!help" or mi == "**":
            clear()
            helpm()
            input("Press Enter To Continue...")
            Menus(1)
        else:
            clear()
            print("WHELP! That didn't quite work...")
            time.sleep(1)
            Menus(1)
                
    elif a == 2:
        clear()
        vulnscans.menu()
        Menus(1)
    elif a == 3:
        clear()
        hashc.start()
        Menus(1)
    elif a == 4:
        clear()
        dos.start()
        Menus(1)
    elif a == 5:
        clear()
        cms.start()
        Menus(1)
    elif a == 6:
        clear()
        sqlmap.start()
        Menus(1)
    elif a == 7:
        clear()
        metasploit.start()
        Menus(1)
    elif a == 8:
        clear()
        dir.start()
        Menus(1)
    else:
        print("WHELP! That didn't quite work...")
        time.sleep(1)
        menu()
        


Menus(1)