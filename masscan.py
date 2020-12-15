import os 
import sys
import re
import time
import vulnscans
import linecache
from clear import clear
from logo import logo, BC

def start():    
    with open('masscan/customArgs.py') as f:
        global customArgs
        customArgs = f.read()
    with open('masscan/target.py') as f:
        global target
        target = f.read()
    with open('masscan/ports.py') as f:
        global ports
        ports = f.read()
    clear()
    menu()
    

def menu():
    logo()
    global customArgs
    global target
    global ports
    m2 = print("Current Block: [" + BC.F + target + BC.G + "]")
    m2 = print("Port(s): [" + BC.F + ports[2:] + BC.G + "]")
    m2 = print("Custom Arguments: [" + BC.F + customArgs + BC.G + "]")
    mitems = ("Set Target", "Set Port(s)", "Clear Ports", "Custom Arguments", "Clear Arguments", "Scan")
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
        print("IE: 127.0.0.0/8")
        target = input("Enter a Target: ")
        with open('masscan/target.py', 'w') as f:
            f.write(target)
        with open('masscan/target.py') as f:
            target = f.read()
        clear()
        menu()
    elif m2 == "2":
        clear()
        print("NOTE: You may add multiple ports with ' - ' and/or ' , '")
        print("IE: 80,800-1000")
        ports = input("Enter Port(s): ")
        with open('masscan/ports.py', 'w') as f:
            f.write('-p' + ports)            
        with open('masscan/ports.py') as f:
            ports = f.read()
        menu()
        #clear()
    elif m2 == "3":
        clear()
        with open('masscan/ports.py', 'w') as f:
            f.write("")
            ports = ""
        menu()        
    elif m2 == "4":
        os.system('masscan -h')
        customArgs = input("Enter Arguments: ")
        with open('masscan/customArgs.py', 'w') as f:
            f.write(' ' + customArgs)
        clear()
        menu()
    elif m2 == "5":
        clear()
        with open('masscan/customArgs.py', 'w') as f:
            f.write("")
            customArgs = ""
        menu()        
    elif m2 == "6":
        os.system('sudo masscan %s %s %s' % (target, ports, customArgs))
        menu()
    elif m2 == "!":
        clear()
        vulnscans.menu()
    elif m2 == "*":
        quit
    elif m2 == "0":
        sys.exit()()