import os 
import sys
import re
import time
import vulnscans
import linecache
from clear import clear
from logo import *

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
    with open('masscan/masscandir.py', 'r') as f:
        global path
        path = f.read()
    clear()
    menu()
    

def menu():
    logo2()
    global customArgs
    global target
    global ports
    global path
    mi = print("Current Block: [" + BC.F + target + BC.G + "]" + BC.F + "       * Global Target Does Not Apply" + BC.G)
    mi = print("Port(s): [" + BC.F + ports[2:] + BC.G + "]")
    mi = print("Custom Arguments: [" + BC.F + customArgs + BC.G + "]")
    mitems("Clear Ports", "Clear Arguments", "Custom Path", "Scan")
    mi = input("")
    mp = mi[:7]
    mo = mi[8:]
    np = mi[:5]
    np2 = mi[5:]
    no = mi[7:]
    na = mi[6:]
    if mi == "1":
        clear()
        with open('masscan/ports.py', 'w') as f:
            f.write("")
            ports = ""
        menu()        
    elif mi == "2":
        clear()
        with open('masscan/customArgs.py', 'w') as f:
            f.write("")
            customArgs = ""
        menu()        
    elif mi == "3":
        clear()
        logo2()
        print("Example Paths: " + BC.F + "/usr/bin/masscan")
        print("               C:/Program Files/SQLMap/masscan" + BC.G)
        print("Note: If you have to launch sqlmap using 'python' please add it before the path.")
        print("")
        path = input("Enter your Masscan file path: ")
        with open('masscan/masscandir.py', 'w') as f:
            f.write(path)
        clear()
        menu()
    elif mi == "4":
        os.system('sudo ' + str(path) + ' %s %s %s' % (ports, target, customArgs))
        menu()
    elif mi == "!":
        clear()
        vulnscans.menu()
    elif mi == "*":
        quit
    elif mi == "0":
        sys.exit()()
    elif mp == "!target":
        print(mp)
        print(mo)
        with open('masscan/target.py', 'w') as f:
            f.write(mo)
        target = mo
        clear()
        menu()
    elif mp == "#target":
        print(mp)
        print(mo)
        target = mo
        clear()
        menu()
    elif np == "#port":
        no = ('-p' + no)
        with open('masscan/ports.py', 'w') as f:
            f.write(no)
        ports = no
        clear()
        menu()
    elif np == "#args":
        clear()
        with open('masscan/customArgs.py', 'w') as f:
            f.write(na)
        customArgs = na
        clear()
        menu()
    elif np == "#help":
        os.system( path + ' --help' )
        input("Press Enter To Continue...")
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