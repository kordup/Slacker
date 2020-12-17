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
    with open('TorsHammer/threads.py') as f:
        global threads
        threads = f.read()
    with open('TorsHammer/customArgs.py') as f:
        global customArgs
        global tor
        tor = ""
        global port
        port = ""
        customArgs = f.read()
        
    global target
    target = globalt.target
    clear()
    menu()
    

def menu():
    logo()
    global threads
    global target
    global port
    global tor
    global customArgs
    print("Current Target: [" + BC.F + target + BC.G + "]")
    mitems("Run")
    mi = input("")
    mp = mi[:7]
    mo = mi[8:]
    np = mi[:5]
    no = mi[6:]
    ba = mi[:8]
    bb = mi[9:]
    aa = mi[4:]
    aa = mi[:5]
    if mi == "1":
        clear()
        os.system('python hulk/hulk.py %s' % (target))
        menu()
        #clear()
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
        os.system( 'python3 hulk/hulk.py --help' )
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