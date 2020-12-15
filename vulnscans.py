import os 
import sys
import re
import nmap
import masscan
import nikto
import linecache
from clear import clear
from logo import logo, BC


#### Add custom args to nmap
def menu():
    clear()
    logo()
    m2 = print("Vuln Scanners")
    mitems = ("Nmap", "Nikto", "Masscan", "Social Engineering Tool Kit")
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
        m2 = input("")
    if m2 == "1":
        nmap.start()
        clear()
    elif m2 == "2":
        nikto.start()
        clear()
    elif m2 == "3":
        masscan.start()
        clear()
    elif m2 == "*":
        quit
    elif m2 == "0":
        sys.exit()()