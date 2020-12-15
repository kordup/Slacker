import os 
import sys
import re
import linecache
from clear import clear
from logo import logo, BC


def menu():
    clear()
    logo()
    m3 = print("Hash Crackers")
    m3 = print("Note: If one of these are not installed, please go install them first.")
    mitems = ("Hashcat", "pyCrack by R00T")
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
        m3 = input("")
    if m3 == "1":
        print("I am one")
        clear()
    elif m3 == "2":
        print("I am Two")
        clear()
    elif m3 == "*":
        quit
    elif m3 == "0":
        sys.exit()