import os 
import sys
import re
import time
import linecache
import vulnscans
from clear import clear
from logo import logo, BC

def start():    
    with open('nikto/proxy.py') as f:
        global proxy
        proxy = f.read()
    with open('nikto/target.py') as f:
        global target
        target = f.read()
    clear()
    menu()
    

def menu():
    logo()
    global proxy
    global target
    print("Current Target: [" + BC.F + target + BC.G + "]")
    print("Current Proxy: [" + BC.F + proxy[11:] + BC.G + "]")
    global menuz
    mitems = ["Set Target", "Use A Proxy", "Clear Proxy", "Scan", "Main Menu"]
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
        proxy = input("Enter a Target: ")
        with open('nikto/target.py', 'w') as f:
            f.write(proxy)
        clear()
        menu()
    elif m2 == "2":
        clear()
        proxy = input("Enter Proxy: ")
        with open('nikto/proxy.py', 'w') as f:
            f.write(' -useproxy ' + proxy)            
        with open('nikto/proxy.py') as f:
            proxy = f.read()
        menu()
        #clear()
    elif m2 == "3":
        clear()
        with open('nikto/proxy.py', 'w') as f:
            f.write("")
            proxy = ""
        menu()        
    elif m2 == "4":
        clear()
        os.system('nikto -h ' + target + proxy)
        menu()
    elif m2 == "!":
        vulnscans.menu()
    elif m2 == "*":
        quit
    elif m2 == "0":
        sys.exit()()