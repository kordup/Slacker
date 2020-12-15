import os 
import sys
import re
import time
import linecache
import vulnscans
from clear import clear
from logo import logo, BC

def start():    
    with open('nmap/customArgs.py') as f:
        global customArgs
        customArgs = f.read()
    with open('nmap/target.py') as f:
        global target
        target = f.read()
    clear()
    menu()
    

def menu():
    logo()
    global customArgs
    global target
    m2 = print("Current Target: [" + BC.F + target + BC.G + "]")
    m2 = print("Custom Arguments: [" + BC.F + customArgs + BC.G + "]")
    mitems = ("Set Target", "Quick Port Scan", "Deep Port Scan", "System Info Scan", "Known Vuln Scan", "Run With Just Custom Arguments", "Custom Arguments", "Clear Arguments")
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "!" + BC.G + "] Vuln Scan Menu")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
        m2 = input("")
    if m2 == "1":
        clear()
        target = input("Enter A Target: ")
        with open('nmap/target.py', 'w') as f:
            f.write(target)
        clear()
        menu()
    elif m2 == "2":
        clear()
        os.system('nmap --top-ports 20 ' + target + customArgs)
        menu()
        #clear()
    elif m2 == "3":
        clear()
        os.system('sudo nmap -v -sS -sV ' + target + customArgs)
        menu()
    elif m2 == "4":
        clear()
        os.system('sudo nmap -O ' + target + customArgs)
        menu()
    elif m2 == "5":
        clear()
        os.system('nmap -Pn --script vuln ' + target + customArgs)
        menu()
    elif m2 == "6":
        clear()
        os.system('sudo nmap ' + target + ' ' + customArgs)
        menu()
    elif m2 == "7":
        os.system('nmap -h')
        customArgs = input("Enter Arguments: ")
        with open('nmap/customArgs.py', 'w') as f:
            f.write(' ' + customArgs)
        clear()
        menu()
    elif m2 == "8":
        with open('nmap/customArgs.py', 'w') as f:
            f.write('')
        clear()
        customArgs = ""
        menu()
    elif m2 == "!":
        vulnscans.menu()
    elif m2 == "*":
        quit
    elif m2 == "0":
        sys.exit()()