import os 
import sys
import re
import time
import linecache
import vulnscans
from clear import clear
from logo import *


def start():
    global target
    with open('hash/target.py', 'r') as f:
        target = f.read()
    clear()
    menu()
    

def menu():
    logo()
    global target
    global leng
    leng = len(target)
    print("Current Hash: %s" % (target))
    print("Hash Length: %s" % (leng))
    mitems2("pyCrack by R00T")
    print(BC.A + '  [ ] HashCat - Coming Soon' + BC.G)
    mi = input("")
    mp = mi[:7]
    mo = mi[8:]
    np = mi[:5]
    no = mi[6:]
    print(leng)
    print(target)
    if mi == "1":
        global htype
        if leng == 32:
            htype = '-m'
            os.system('python3 pyCrack.py -m %s' % (target))
            print('python3 pyCrack.py %s %s' % (htype, target))
            menu()
        elif leng == 64:
            htype = '-S'
            os.system('python3 pyCrack.py -S %s' % (target))
            print('python3 pyCrack.py -S %s' % (target))
            menu()
        elif leng == 40:
            htype = '-s'
            os.system ( 'python3 pyCrack.py -s %s' % ( target ))
            print("python3 pyCrack.py -s " + target)
            menu()
        else:
            clear()
            print(BC.F + "Hash Type Unknown" + BC.G)
            menu()
    elif mi == "2":
        exit     
    elif mi == "3":
        exit
    elif mi == "*":
        clear()
        quit
    elif mi == "0":
        sys.exit()()
    elif mp == "!target":
        with open('hash/target.py', 'w') as f:
            f.write(mo)
        target = mo
        clear()
        menu()
    elif mp == "#target":
        with open('hash/target.py', 'w') as f:
            f.write(mo)
        target = mo
        clear()
        start()
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