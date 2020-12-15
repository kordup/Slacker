import os 
from clear import clear
from logo import logo, BC
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
######### Add Nikto, Masscan, Hashcat to install script
######### Add SE Tool Kit
######### Finish CMS Tools
######### Add DoS Tools
######### Add Dir Tools, Admin Finder


### Main Menu(s) ###
def Menus(a):
    if a == 1:
        clear()
        logo()
        print("What type of trouble are we looking for?")
        mitems = ("Vulnerability Scans", "Hash Cracking", "DoS", "CMS Check and Vuln Check", "SQLMap*", "Metasploit*", "Web Dir/File Crawlers")
        for idx, i in enumerate(mitems, start=1):
            print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
        else:
            print("------------------------------------------")
            print(" [" + BC.F + "0" + BC.G + "] Exit")
            m1 = input("")
        if m1 == "1":
            Menus(2)
        elif m1 == "2":
            Menus(3)
        elif m1 == "3":
            Menus(4)
        elif m1 == "4":
            Menus(5)
        elif m1 == "5":
            Menus(6)
        elif m1 == "6":
            Menus(7)
        elif m1 == "7":
            Menus(8)
        elif m1 == "8":
            Menus(9)
        elif m1 == "0":
            quit
            
    elif a == 2:
        clear()
        vulnscans.menu()
        Menus(1)
    elif a == 3:
        clear()
        hashc.menu()
        Menus(1)
    elif a == 4:
        clear()
        dos.menu()
        Menus(1)
    elif a == 5:
        clear()
        cms.menu()
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
        dir.menu()
        Menus(1)


Menus(1)