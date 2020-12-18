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
    global ua
    ua = False
    global customArgs
    customArgs = ""
    global target
    target = globalt.target
    clear()
    menu()
    

def menu():
    logo()
    global proxy
    global target
    global customArgs
    print("Current Target: [" + BC.F + target + BC.G + "]")
    print("Custom Arguments: [" + BC.F + customArgs + BC.G + "]")
    print("User Agents: [" + BC.F + ua + BC.G + "]")
    mitems("Scan", "Toggle User Agents")
    mi = input("")
    mp = mi[:7]
    mo = mi[8:]
    np = mi[:5]
    no = mi[6:]
    if mi == "1":
        clear()
        os.system('IPGeoLocation/ipgeolocation.py %s -t %s' % (customArgs, target))
        menu()
        #clear()
    if mi == "1":
        if ua == False:
            ua = True
        elif ua == True:
            ua = False
        userAgents = "-U "
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
        os.system( 'IPGeoLocation/ipgeolocation.py --help' )
        input("Press Enter To Continue...")
        menu()
    elif np == "!help" or mi == "**":
        clear()
        helpm()
        input("Press Enter To Continue...")
        menu()
    elif np == "#args":
        with open('ipgeo/customArgs.py', 'w') as f:
            f.write(no)
        customArgs = no
        clear()
        menu()
    else:
        clear()
        print("WHELP! That didn't quite work...")
        time.sleep(1)
        menu()