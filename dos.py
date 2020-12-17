import os 
import sys
import re
import time
import linecache
import globalt
import torshammer
import hulk
import vulnscans
from clear import clear
from logo import *

def start(): 
    global target
    target = globalt.target
    clear()
    menu()
    

def menu():
    logo()
    global target
    mitems2("TorsHammer", "The Hulk")
    mi = input("")
    mp = mi[:7]
    mo = mi[8:]
    np = mi[:5]
    no = mi[6:]
    if mi == "1":
        torshammer.start()
    elif mi == "2":
        hulk.start()
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
        clear()
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