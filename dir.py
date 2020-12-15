import os 
import sys
import re
import linecache
from clear import clear
from logo import logo, BC


def menu():
    clear()
    logo()
    m2 = print("Dir/File Scanners")
    mitems = ("DirBuster", "Subdomainer", "Admin Page Finder")
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
        m2 = input("")
    if m2 == "1":
        print("I am one")
        clear()
    elif m2 == "2":
        print("I am Two")
        clear()
    elif m2 == "3":
        print("I am Three")
        clear()
    elif m2 == "*":
        quit
    elif m2 == "0":
        sys.exit()()