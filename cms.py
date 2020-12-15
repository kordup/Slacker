import os 
import sys
import re
import linecache
from clear import clear
from logo import logo, BC


def menu():
    clear()
    logo()
    m5 = print("CMS Check and Vuln Checkers")
    mitems = ("JoomScan", "WPScan", "DroopalScan", "CMSTool for auto CMS Check/Vuln Scan")
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
        m5 = input("")
    if m5 == "1":
        clear()
        print("I am one")
        menu()
    elif m5 == "2":
        clear()
        print("I am Two")
        menu()
    elif m5 == "3":
        clear()
        print("I am Three")
        menu()
    elif m5 == "4":
        clear()
        print("I am Four")
        menu()
    elif m5 == "*":
        quit
    elif m5 == "0":
        sys.exit()